from django.test import TestCase
from gallery.models import Post, PostManager, UserProfile
from django.contrib.auth.models import User


class UTestCase(TestCase):
    def test_index_loads_properly(self):
        response = self.client.get('127.0.0.1:8000')
        self.assertEqual(response.status_code, 404)
    def test_index_loads_properly(self):
        response = self.client.get('192.168.0.0:9000')
        self.assertEqual(response.status_code, 404)