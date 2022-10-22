from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from http import HTTPStatus


class RegisterTestCase(TestCase):
    
    def setUp(self):
        url = reverse('register')
        self.response = self.client.get(url)
    
    def test_register_template(self):
        self.assertEqual(self.response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(self.response, 'register.html')
        self.assertContains(self.response, 'Register')
        self.assertNotContains(self.response, 'Hi there! I should not be on the page.')
        

class SignInTestCase(TestCase):
    
    def setUp(self):
        url = reverse('signin')
        self.response = self.client.get(url)
    
    def test_signin_template(self):
        self.assertEqual(self.response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(self.response, 'signin.html')
        self.assertContains(self.response, 'Sign In')
        self.assertNotContains(self.response, 'Hi there! I should not be on the page.')
