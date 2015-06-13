from django.test import TestCase
from django.contrib.auth.models import User


class TestNucleoApi(TestCase):
    '''API TESTs'''

    fixtures = ['user.json', 'post.json']

    def setUp(self):
        self.mock_user = {
            'email': 'g0ph@g0ph.com',
            'name': 'g0ph',
            'password': 'g0ph',
        }
        # User.objects.create_user(self.mock_user['name'],
        #                          self.mock_user['email'],
        #                          self.mock_user['password'])
        self.client.login(
            username=self.mock_user['name'],
            password=self.mock_user['password'],
        )
        # Each self.client.get show pass follow=True

    def test_following(self):
        response = self.client.post('/api/following', {})
        print response
        assert False
