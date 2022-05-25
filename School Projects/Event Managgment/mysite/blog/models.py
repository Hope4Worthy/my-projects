from django.db import models
from django.contrib.auth.models import User, Group
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from datetime import timedelta
from django.urls import reverse
from autoslug import AutoSlugField
from django.utils.text import slugify
from django.shortcuts import redirect
from django.core.exceptions import ValidationError

RSO_STATUS = (
    ('INACTIVE','inactive'),
    ('ACTIVE','active')
)
STATUS = (
    (0,"Pending"),
    (1,"Approved"),
    (2,"Passed")
)

RATINGS = (
    (1, 'poor'),
    (2, 'fair'),
    (3, 'average'),
    (4, 'good'),
    (5, 'great')
)

EVENT_TYPES = (
    (1, 'public'),
    (2, 'rso'),
    (3, 'private')
)

CHOICES = (
    1,2
)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        instance.groups.add(Group.objects.get(name='student'))
        uniSet = University.objects.all()
        for uni in uniSet:
            if uni.domain in instance.email:
                uni.students.add(instance)


class University(models.Model):
    name = models.CharField(max_length=50)
    domain = models.CharField(max_length=30, blank=False)
    description = models.TextField()
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    studentPopulation = models.IntegerField()
    students = models.ManyToManyField(User,  related_name='university', blank=True)
    admin = models.ForeignKey(User, on_delete=models.CASCADE, related_name='uniAdmin', limit_choices_to={'groups':3})

    class Meta:
        ordering = ['-studentPopulation']
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('event_list_active')

class Location(models.Model):
    name = models.CharField(max_length=50)
    latitude = models.FloatField()
    longitude = models.FloatField()
    university = models.ForeignKey(University, on_delete = models.CASCADE, related_name='locationUniversity')
    description = models.TextField()

    class Meta:
        ordering = ['-university']
    
    def __str__(self):
        return ('{} at  {}'.format(self.name, self.university.name))

    def get_absolute_url(self):
        return reverse('event_list_active')

class Rso(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=250)
    university = models.ForeignKey(University, on_delete = models.CASCADE, related_name='rsoUniversity')
    owner = models.ForeignKey(User, limit_choices_to={'groups':2}, on_delete = models.CASCADE, related_name='rsoOwner', blank=True)
    students = models.ManyToManyField(User, limit_choices_to={'groups':CHOICES}, blank=True)
    numberOfMembers = models.IntegerField(default=4)
    status = models.CharField(choices=RSO_STATUS, default='INACTIVE', max_length=8)
    slug = models.SlugField(max_length=200, unique=True)

    def total_students(self):
        count = self.students.count()
        self.active = count 
        return count

    def __str__(self):
        return '{} at {}'.format(self.name, self.university.name)
    
    def get_absolute_url(self):
        return reverse('rso_list')

@receiver(post_save, sender=Rso)
def rso_post_save(sender, instance, **kwargs):
    instance.numberOfMembers = instance.students.count()
    if instance.total_students() < 4:
        instance.status = "INACTIVE"
    else:
        instance.status = "ACTIVE"
    

class Event(models.Model):
    name = models.CharField(max_length=100)
    university = models.ForeignKey(University, on_delete=models.CASCADE, related_name='university')
    description = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    atendee = models.ManyToManyField(User)
    host = models.ForeignKey(Rso, on_delete=models.CASCADE, blank=True, null=True, related_name='eventHost')
    day = models.DateField(u'Day of the event', help_text=u'Day of the event')
    start_time = models.TimeField(u'Starting time', help_text=u'Starting time')
    end_time = models.TimeField(u'Final time', help_text=u'Final time')
    event_type = models.IntegerField(choices=EVENT_TYPES, default=1)
    created_on = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, default=1, related_name='creator')
 
    def check_overlap(self, fixed_start, fixed_end, new_start, new_end):
        overlap = False
        if new_start == fixed_end or new_end == fixed_start:    #edge case
            overlap = False
        elif (new_start >= fixed_start and new_start <= fixed_end) or (new_end >= fixed_start and new_end <= fixed_end): #innner limits
            overlap = True
        elif new_start <= fixed_start and new_end >= fixed_end: #outter limits
            overlap = True
 
        return overlap
 
    def get_absolute_url(self):
        return reverse('event_list_active')

    def verify(self):
        self.status=1
        self.save()
    
    def add_user(self, user):
        self.atendee.add(user)
        self.save()

    def remove_user(self, user):
        self.atendee.remove(user)
        self.save()

    def clean(self):
        if self.end_time <= self.start_time:
            raise ValidationError('Ending times must after starting times')
 
        events = Event.objects.filter(day=self.day)
        if events.exists():
            for event in events:
                if not self == event:
                    if self.location == event.location:
                        if self.check_overlap(event.start_time, event.end_time, self.start_time, self.end_time):
                            raise ValidationError(
                                'There is an overlap with ' + event.name + ' event on: ' + str(event.day) + ', ' + str(
                                    event.start_time) + '-' + str(event.end_time))


@receiver(pre_save, sender=Event)
def event_pre_save(sender, instance, **kwargs):
    if instance.event_type != 1:
        instance.status = 1
    elif instance.status == 0:
        if instance.host:
            instance.status = 1

class Comment(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=50)
    author = models.ForeignKey(User, on_delete = models.CASCADE, related_name='author')
    body = models.TextField()
    rating = models.IntegerField(choices=RATINGS, default=5)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']
    
    def __str__(self):
        return 'comment {} by {}'.format(self.name, self.author)
    
    def get_absolute_url(self):
        return reverse('event_detail', kwargs={'pk':self.event.id})
        #return dispatch_view(request, self.event.slug)


