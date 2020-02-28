from django.contrib import admin
from .models import Meeting, Minutes, Resource, Event
# Register your models here.

admin.site.register(Meeting)
admin.site.register(Minutes)
admin.site.register(Resource)
admin.site.register(Event)