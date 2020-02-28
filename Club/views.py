from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Event, Meeting, Minutes, Resource
from django.contrib.auth.decorators import login_required
from .forms import MeetingForm
from .forms import ResourceForm
from .forms import EventForm

# Create your views here.
def index (request):
    return render(request, 'club/index.html')

def getresources(request):
    resource_list=Resource.objects.all()
    return render(request, 'club/resources.html' , {'resource_list' : resource_list})

def getevents(request):
    event_list=Event.objects.all()
    return render(request, 'club/events.html' , {'event_list' : event_list})

def getmeetings(request):
    meeting_list=Meeting.objects.all()
    return render(request, 'club/meetings.html' , {'meeting_list' : meeting_list})

def meetingdetails(request, id):
    meet=get_object_or_404(Meeting, pk=id) 
    #mmin=Minutes.objects.filter(Meeting, pk=id)
    context={
        'meet' : meet,
        #'mmin' : mmin,
    }
    return render(request, 'Club/meetingdetails.html', context=context)

def meetingminutes(request, id):
    mmin=get_object_or_404(Meeting, pk=id)
    context={
        'mmin' : mmin,
    }
    return render(request, 'Club/meetingminutes.html', context=context)

def loginmessage(request):
    return render(request, 'club/loginmessage.html')

def logoutmessage(request):
    return render(request, 'club/logoutmessage.html')


@login_required
def newMeeting(request):
     form=MeetingForm
     if request.method=='POST':
          form=MeetingForm(request.POST)
          if form.is_valid():
               post=form.save(commit=True)
               post.save()
               form=MeetingForm()
     else:
          form=MeetingForm()
     return render(request, 'Club/newmeeting.html', {'form': form})

@login_required
def newResource(request):
     form=ResourceForm
     if request.method=='POST':
          form=ResourceForm(request.POST)
          if form.is_valid():
               post=form.save(commit=True)
               post.save()
               form=ResourceForm()
     else:
          form=ResourceForm()
     return render(request, 'Club/newresource.html', {'form': form})

@login_required
def newEvent(request):
     form=EventForm
     if request.method=='POST':
          form=EventForm(request.POST)
          if form.is_valid():
               post=form.save(commit=True)
               post.save()
               form=EventForm()
     else:
          form=EventForm()
     return render(request, 'Club/newevent.html', {'form': form})