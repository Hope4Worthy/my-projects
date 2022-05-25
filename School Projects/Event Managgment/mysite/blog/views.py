from .models import *
from .forms import *
from django.views import generic
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import Group
from django.core.exceptions import ValidationError

STATUS = (
    (0,"Pending"),
    (1,"Approved"),
    (2,"Passed")
)

def initial_redirect(request):
    return redirect('user_login')

def event_add(request):
    form = EventForm(request.POST or None)
    if University.objects.filter(students = request.user).exists():
        universities = University.objects.get(students = request.user)
        locations = Location.objects.filter(university = universities)
    else:
        universities = University.objects.all()
        locations = Location.objects.all()
    form.fields['location'].queryset = locations

    rsos = Rso.objects.filter(students = request.user)
    form.fields['host'].queryset = rsos
    context = {'form':form}

    if form.is_valid():
        instance = form.save(commit = False)
        instance.creator = request.user
        if University.objects.filter(students = user).exists():
            instance.university = University.objects.get(students = request.user)
        else:
            instance.university = University.objects.get(admin = request.user)

        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())

    return render(request, 'event_add.html', context)

class event_detail(generic.DetailView):
    model = Event
    template_name = 'event_detail.html'

class event_list_active(LoginRequiredMixin, generic.ListView):
    model = Event
    template_name = 'event_list.html'

    def get_queryset(self):
        user = self.request.user
        qs1 = Event.objects.filter(status=1) # active events
        if University.objects.filter(students = user).exists():
            queryset = qs1.filter(event_type=1) # public events
            queryset = queryset | qs1.filter(event_type=3).filter(university=University.objects.get(students = user)) # private events at the users
            for rso in Rso.objects.filter(students = user):
                queryset = queryset | qs1.filter(host=rso)
            return queryset
        return None

class event_list_pending(generic.ListView):
    queryset = Event.objects.filter(status=0).order_by('-created_on')
    template_name = 'event_verify.html'

class event_edit(generic.UpdateView):
    model = Event
    template_name = 'event_edit.html'
    form_class = EventForm

def event_join(request, pk):
    event = Event.objects.get(id = pk)
    event.add_user(request.user.id)
    return redirect('event_detail', pk)

def event_leave(request, pk):
    event = Event.objects.get(id = pk)
    event.remove_user(request.user.id)
    return redirect('event_detail', pk)

def event_verify(request, pk):
    event = Event.objects.get(id = pk)
    event.verify()
    return redirect('event_detail', pk)

def event_delete(request, pk):
    event = Event.objects.get(id = pk)
    event.delete()
    return redirect('event_list_active')



class rso_add(generic.CreateView):
    model = Rso
    template_name = 'rso_add.html'
    form_class = RsoForm

    def form_valid(self, form):
        form.instance.owner = self.request.user
        self.request.user.groups.add(Group.objects.get(name='admin'))
        form.instance.university = University.objects.get(students = self.request.user)
        return super().form_valid(form)

class rso_detail(generic.DetailView):
    model = Rso
    template_name = 'rso_detail.html'

class rso_list(LoginRequiredMixin, generic.ListView):
    model = Rso
    template_name = 'rso_list.html'

    def get_queryset(self):
        user = self.request.user
        qs1 = Rso.objects.none()
        if University.objects.filter(students = user).exists():
            qs1 = Rso.objects.filter(university=University.objects.get(students = user)) # rso's at users university
            return qs1
        elif University.objects.filter(admin = user).exists(): # user is superAdmin
            for university in University.objects.filter(admin = user):
                qs1 = qs1 | Rso.objects.filter(university=university) # get RSO's at all universies that the superAdmin has made
            return qs1
        return None

def rso_join(request, pk):
    rso = Rso.objects.get(id = pk)
    rso.students.add(request.user)
    return redirect('rso_detail', pk)

def rso_leave(request, pk):
    rso = Rso.objects.get(id = pk)
    rso.students.remove(request.user)
    return redirect('rso_detail', pk)

class rso_edit(generic.UpdateView):
    model = Rso
    template_name = 'rso_edit.html'
    form_class = RsoForm

    def get_success_url(self):
        return reverse('rso_detail', kwargs={"pk":self.kwargs['pk']})

def rso_delete(request, pk):
    rso = Rso.objects.get(id = pk)
    rso.delete()
    return redirect('rso_list')



def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect(reverse('event_list_active'))
        else:
            messages.error(request,"Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="user_login.html", context={"login_form":form})

def user_register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful." )
            return redirect(reverse('user_login'))
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render (request=request, template_name="user_register.html", context={"register_form":form})



class university_add(LoginRequiredMixin, generic.CreateView):
    model = University
    template_name = 'university_add.html'    
    fields = ('name', 'domain','city','state', 'studentPopulation','description')
    def form_valid(self, form):
        form.instance.admin = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('university_list')

class university_edit(generic.UpdateView):
    model = University
    template_name = 'university_edit.html'
    fields = ('name', 'domain','city','state', 'studentPopulation','description')

    def get_success_url(self):
        return reverse('university_detail', kwargs={"pk":self.kwargs['pk']})

class university_list(LoginRequiredMixin, generic.ListView):
    model = University
    template_name = 'university_list.html'

    def get_queryset(self):
        user = self.request.user
        if University.objects.filter(admin = user).exists(): # user is superAdmin
            qs1 = University.objects.filter(admin=self.request.user) # universites that the superAdmin is a admin of
            return qs1
        return None

class university_detail(generic.DetailView):
    model = University
    template_name = 'university_detail.html'

class location_add(generic.CreateView):
    model = Location
    template_name = 'location_add.html'    
    fields = ('name', 'latitude','longitude','university','description')

    def get_success_url(self):
        return reverse('location_list')

class location_edit(generic.UpdateView):
    model = Location
    template_name = 'location_edit.html'
    fields = ('name', 'latitude','longitude','university','description')

    def get_success_url(self):
        return reverse('location_detail', kwargs={"pk":self.kwargs['pk']})

class location_list(LoginRequiredMixin, generic.ListView):
    model = Location
    template_name = 'location_list.html'

    #def get_queryset(self):
        #user = self.request.user
        #qs1 = Location.objects.none()
        #if University.objects.filter(admin = user).exists(): # user is superAdmin
            #for university in University.objects.filter(admin=self.request.user):
                #qs1 = qs1 | Location.objects.filter(university=university)
            #return qs1
        #return Location.objects.all()

class location_detail(generic.DetailView):
    model = Location
    template_name = 'location_detail.html'

def location_delete(request, pk):
    location = Location.objects.get(id = pk)
    location.delete()
    return redirect('location_list')



class comment_add(generic.CreateView):
    model = Comment
    template_name = 'comment_add.html'
    form_class = CommentForm

    def form_valid(self, form):
        form.instance.event_id = self.kwargs['pk']
        form.instance.author = self.request.user
        return super().form_valid(form)

def comment_delete(request, epk, cpk):
    comment = Comment.objects.get(id = cpk)
    comment.delete()
    return redirect('event_detail', epk)

class comment_edit(generic.UpdateView):
    model = Comment
    template_name = 'comment_edit.html'
    fields = ('name', 'rating','body')
