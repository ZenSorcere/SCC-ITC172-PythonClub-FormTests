from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('getresources/', views.getresources, name='resources'),
    path('getmeetings/', views.getmeetings, name='meetings'),
    path('meetingdetails/<int:id>', views.meetingdetails, name='meetingdetails'),
    path('getevents/', views.getevents, name='events'),
    path('meetingminutes/<int:id>', views.meetingminutes, name='meetingminutes'),

    path('newMeeting/', views.newMeeting, name='newmeeting'),
    path('newResource/', views.newResource, name='newresource'),
    path('newEvent/', views.newEvent, name='newevent'),

    path('loginmessage/', views.loginmessage, name='loginmessage'),
    path('logoutmessage/', views.logoutmessage, name='logoutmessage'),
]
