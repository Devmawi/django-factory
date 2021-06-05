from django.http.response import HttpResponse
from django.test import TestCase, client
from . import models
from django.test import Client
from django.contrib.auth import get_user_model

# Create your tests here.
class MachinesIndexTest(TestCase):

    def setUp(self):
        User = get_user_model()
        User.objects.create_user('admin', None, 'admin')

    def test_assert_true(self):
        machines = models.Machine.objects.all()
        self.assertIsNotNone(machines)

    def test_assert_redirect(self):
        client = Client()  
        
        res:HttpResponse = client.get('/machines')
        self.assertEqual(res.status_code, 301)

        logged_in = client.login(username='admin', password='admin')
        self.assertTrue(logged_in)

        res:HttpResponse = client.get('/machines', follow=True)
        self.assertEqual(res.status_code, 200)