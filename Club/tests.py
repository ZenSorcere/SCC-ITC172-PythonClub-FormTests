from django.test import TestCase
from .models import Meeting, Minutes, Resource, Event
from .views import index, getmeetings, getresources, newMeeting
from django.contrib.auth.models import User
from django.urls import reverse
from .forms import MeetingForm, EventForm, ResourceForm

class MinutesTest(TestCase):
    def test_string(self):
        minutes=Minutes(Meeting.mtgId=='1') #minutes_id
        self.assertEqual(str(minutes), str(Meeting.mtgId)) #minutes_id

    def test_table(self):
        self.assertEqual(str(Minutes._meta.db_table), 'minutes')

class MeetingTest(TestCase):
    def test_string(self):
        mtg=Meeting(mtgtitle="Test Meeting")
        self.assertEqual(str(mtg), mtg.mtgtitle)

    def test_table(self):
        self.assertEqual(str(Meeting._meta.db_table), 'meeting')

class EventTest(TestCase):
    def test_string(self):
        event=Event(eventtitle="Lab")
        self.assertEqual(str(event), event.eventtitle)

    def test_table(self):
        self.assertEqual(str(Event._meta.db_table), 'event')

class ResourcesTest(TestCase):
    #set up one time sample data
    def setup(self):
        type = Resource(resourcetype='stapler')
        res=Resource(resourcename='Redline', resourcetype='stapler', resourcedesc='Important office tool')
        return res

    def test_string(self):
        res = self.setup()
        #res=Resource(resourcename="stapler")
        self.assertEqual(str(res), res.resourcename)

    def test_type(self):
        res=self.setup()
        self.assertEqual(str(res.resourcetype), 'stapler')

    def test_table(self):
        self.assertEqual(str(Resource._meta.db_table), 'resource')

# Views Test cases -- minus "meeting details", which looks like it would require a bunch of setup
class IndexTest(TestCase):
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

class GetMeetings(TestCase):
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('meetings'))
        self.assertEqual(response.status_code, 200)

class GetResources(TestCase):
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('resources'))
        self.assertEqual(response.status_code, 200)

class GetEvents(TestCase):
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('events'))
        self.assertEqual(response.status_code, 200)

# Testing for authenticated users, using the resources form
class New_Resource_authentication_test(TestCase):
    def setUp(self):
        self.test_user=User.objects.create_user(username='testuser1', password='P@ssw0rd1')
        self.name='redline'
        self.type='stapler'
        self.date='2019-04-02'
        self.prod = Resource.objects.create(resourcename=self.name, resourcetype=self.type, dateentered=self.date, user=self.test_user, resourceurl= 'http://www.officedepo.com', resourcedesc="Important office tool")
        return self.setUp

    def test_redirect_if_not_logged_in(self):
        response=self.client.get(reverse('newresource'))
        self.assertRedirects(response, '/accounts/login/?next=/Club/newResource/')

    def test_Logged_in_uses_correct_template(self):
        login=self.client.login(username='testuser1', password='P@ssw0rd1')
        response=self.client.get(reverse('newresource'))
        self.assertEqual(str(response.context['user']), 'testuser1')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Club/newresource.html')

class New_Meeting_Form_Test(TestCase):
    #def setUp(self):
     #   self.test_user=User.objects.create_user(username='testuser1')
      #  self.mtg=Meeting.objects.create(mtgId='1')
       # self.title=Meeting.objects.create(mtgtitle='test meeting')
        #self.date=Meeting.objects.create(mtddate='2019-04-02')
        #self.time='10:00'
        #self.agenda='test things'
        #self.prod = Meeting.objects.create(mtgtitle=self.title, user=self.test_user, mtgdate=self.date, mtgtime=self.time, mtglocation= 'Denali', agenda=self.agenda)

    def test_typeform_is_valid(self):
        form=MeetingForm(data={'mtgId': "1", 'mtgtitle': "Test Meeting", 'mtgdate': "2020-01-20", 'mtgtime': "10am", 'mtglocation':"Denali", 'agenda': "test things"})
        self.assertTrue(form.is_valid())

    def test_typeform_minus_location(self):
        form=MeetingForm(data={'mtglocation':""})
        self.assertFalse(form.is_valid())

class Resource_Form_Test(TestCase):
    def test_typeform_is_valid(self):
        self.test_user=User.objects.create_user(username='testuser1', password='P@ssw0rd1')
        form=ResourceForm(data={'resourcename': "redline", 'resourcetype': "stapler", 'resourceurl': "http://www.officedepo.com", 'dateentered': "2019-04-02", 'user': self.test_user, 'resourcedesc': "import office tool"})
        self.assertTrue(form.is_valid())

    def test_typeform_minus_resourcetype(self):
        form=ResourceForm(data={'resourcetype': ""})
        self.assertFalse(form.is_valid())

    def test_typeform_empty(self):
        form=ResourceForm(data={'resourcedesc': ""})
        self.assertFalse(form.is_valid())

class Event_Form_Test(TestCase):
    def test_typeform_is_valid(self):
        self.test_user=User.objects.create_user(username='testuser1', password='P@ssw0rd1')
        form=EventForm(data={'eventtitle': "testevent", 'eventlocation': "Rainier", 'eventdate': "2019-04-02", 'eventtime': "10:00", 'eventdesc': "cool event", 'user': self.test_user})
        self.assertTrue(form.is_valid())
    
    def test_typeform_minus_location(self):
        form=EventForm(data={'eventlocation': ""})
        self.assertFalse(form.is_valid())

    def test_typeform_empty(self):
        form=EventForm(data={'eventtitle': ""})
        self.assertFalse(form.is_valid())

    
