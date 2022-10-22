from django.test import TestCase
from django.urls import reverse
from http import HTTPStatus


class HomeTestCase(TestCase):
    
    def setUp(self):
        url = reverse('home')
        self.response = self.client.get(url)
    
    def test_home_template(self):
        self.assertEqual(self.response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(self.response, 'home.html')
        self.assertContains(self.response, 'Restaurants')
        self.assertContains(self.response, 'Mavhungu Adivhaho')
        self.assertNotContains(self.response, 'Hi there! I should not be on the page.')