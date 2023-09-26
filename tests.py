from django.test import TestCase
from polls.models import ProfileUser

class UserTestCase(TestCase):
    def setUp(self):
        ProfileUser.objects.create(username="Michaella", email="mick@gmail.com")
    
    def test_name(self):
        mick_name = ProfileUser.objects.get(username="Michaella")
        self.assertEqual(mick_name.username, 'Michaella') 
    
    def test_email(self):
        mick_mail = ProfileUser.objects.get(email="mick@gmail.com")
        self.assertEqual(mick_mail.email, 'mick@gmail.com')

