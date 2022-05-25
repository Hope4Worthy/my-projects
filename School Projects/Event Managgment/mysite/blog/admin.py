from django.contrib import admin
from datetime import timedelta
from .models import *
from django.db.models import Count
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    fields = ['name']
    actions = ['approve_event','set_passed']

    def approve_event(self, request, queryset):
        queryset.update(status = 1)
    
    def set_passed(self, request, queryset):
        queryset.update(status = 1)
    
    def save_model(self, request, obj, form, change):
        if not change:
            if(obj.event_type == 1):
                if not obj.host:
                    obj.status = 0
                else:
                    obj.status = 1
            else:
                obj.status = 1
        obj.save()

@admin.register(University)
class UniversityAdmin(admin.ModelAdmin):
    list_display = ('name', 'domain', 'studentPopulation','state', 'city')
    list_filter = ("name",)
    search_fields = ['name', 'domain', 'state', 'city']

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'university', 'latitude','longitude')
    list_filter = ('name', 'university',)
    search_fields = ['name', 'university']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name','rating','body','event', 'created_on')
    list_filter = ('rating','created_on')
    search_fields = ('name', 'body')
    actions = ['approve_comments']

@admin.register(Rso)
class RsoAdmin(admin.ModelAdmin):
    list_display = ('name', 'university','owner','description', 'status', 'numberOfMembers')
    list_filter = ('name','university','owner')
    search_fields = ('name','university','owner')
    fields = ['name','owner','university','description','students', 'slug']
    prepopulated_fields = {'slug': ('name',)}

    def save_model(self, request, obj, form, change):
        obj.save()
        obj.numberOfMembers = obj.students.all().count()
        if change:
            i = obj.numberOfMembers
            if i >= 4:
                obj.status = 1
            else:
                obj.status = 0
        obj.numberOfMembers = obj.students.all().count()
        obj.save()

