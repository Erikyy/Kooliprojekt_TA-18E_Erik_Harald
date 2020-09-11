from django.test import TestCase, RequestFactory
from gallery.models import Post, PostManager, UserProfile
from django.contrib.auth.models import AnonymousUser, User
from gallery.views import home


class UTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='Test1', email='test@test.com', password='top_secret'
        )
    def test_index_loads_properly(self):
        response = self.client.get('http://127.0.0.1:8000')
        print(response)
        self.assertEqual(response.status_code, 200)

    def test_home(self):
        request = self.factory.get('/testing/details')
        request.user = self.user

        response = home(request)
        self.assertEqual(response.status_code, 200)


