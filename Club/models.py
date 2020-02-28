from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Meeting(models.Model):
    mtgId=models.SmallIntegerField()
    mtgtitle=models.CharField(max_length=255)
    mtgdate=models.DateField()
    mtgtime=models.TimeField()
    mtglocation=models.CharField(max_length=255, null=True, blank=True)
    agenda=models.TextField()

    def __str__(self):
        return self.mtgtitle
    
    class Meta:
        db_table='meeting'
        verbose_name_plural='meetings'

class Minutes(models.Model):
    mtgId=models.ForeignKey(Meeting, on_delete=models.DO_NOTHING)
    attendance=models.ManyToManyField(User)
    minutestext=models.TextField()

    def __str__(self):
        return str(Meeting.mtgId) #minutes_id
    
    class Meta:
        db_table='minutes'
        verbose_name_plural='minutes'

class Resource(models.Model):
    resourcename=models.CharField(max_length=255)
    resourcetype=models.CharField(max_length=255, null=True, blank=True)
    resourceurl=models.URLField(null=True, blank=True)
    dateentered=models.DateField(null=True, blank=True)
    user=models.ForeignKey(User, on_delete=models.DO_NOTHING)
    resourcedesc=models.TextField()

    def __str__(self):
        return self.resourcename
    
    class Meta:
        db_table='resource'
        verbose_name_plural='resources'

class Event(models.Model):
    eventtitle=models.CharField(max_length=255)
    eventlocation=models.CharField(max_length=255, null=True, blank=True)
    eventdate=models.DateField()
    eventtime=models.TimeField()
    eventdesc=models.TextField()
    user=models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.eventtitle
    
    class Meta:
        db_table='event'
        verbose_name_plural='events'