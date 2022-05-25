from . import views
from django.urls import path, re_path
import djhacker
from .models import *

urlpatterns = [
    path("",                                            views.initial_redirect,             name='initial_redirect'),

    path('event/add/',                                  views.event_add,                    name='event_add'),
    path('event/<int:pk>/',                             views.event_detail.as_view(),       name='event_detail'),
    path('event/<int:pk>/edit/',                        views.event_edit.as_view(),         name='event_edit'),
    path('event/<int:pk>/verify/',                      views.event_verify,                 name='event_verify'),
    path('event/<int:pk>/join/',                        views.event_join,                   name='event_join'),
    path('event/<int:pk>/leave/',                       views.event_leave,                  name='event_leave'),
    path('event/<int:pk>/delete/',                      views.event_delete,                 name='event_delete'),
    path('event/<int:pk>/comment/create/',              views.comment_add.as_view(),        name='comment_add'),
    path('event/<int:epk>/comment/<int:cpk>/delete/',   views.comment_delete,               name='comment_delete'),
    path('event/comment/<int:pk>/edit/',                views.comment_edit.as_view(),       name='comment_edit'),
    path('event/list/active',                           views.event_list_active.as_view(),  name='event_list_active'),
    path('event/list/pending',                          views.event_list_pending.as_view(), name='event_list_pending'),

    path('rso/list/',                                   views.rso_list.as_view(),           name='rso_list'),
    path('rso/create/',                                 views.rso_add.as_view(),            name='rso_add'),
    path('rso/details/<int:pk>/',                       views.rso_detail.as_view(),         name='rso_detail'),
    path('rso/details/<int:pk>/join/',                  views.rso_join,                     name='rso_join'),
    path('rso/details/<int:pk>/leave/',                 views.rso_leave,                    name='rso_leave'),
    path('rso/details/<int:pk>/edit/',                  views.rso_edit.as_view(),           name='rso_edit'),
    path('rso/details/<int:pk>/delete/',                views.rso_delete,                   name='rso_delete'),

    path('user/login/',                                 views.user_login,                   name='user_login'),
    path("user/register/",                              views.user_register,                name="user_register"),

    path('university/list/',                            views.university_list.as_view(),    name='university_list'),
    path('university/add/',                             views.university_add.as_view(),     name='university_add'),
    path('university/<int:pk>/detail',                  views.university_detail.as_view(),  name='university_detail'),
    path('university/<int:pk>/edit',                    views.university_edit.as_view(),    name='university_edit'),

    path('location/list/',                              views.location_list.as_view(),      name='location_list'),
    path('location/add/',                               views.location_add.as_view(),       name='location_add'),
    path('location/<int:pk>/detail',                    views.location_detail.as_view(),    name='location_detail'),
    path('location/<int:pk>/edit',                      views.location_edit.as_view(),      name='location_edit'),
    path('location/<int:pk>/delete',                    views.location_delete,              name='location_delete'),
]
