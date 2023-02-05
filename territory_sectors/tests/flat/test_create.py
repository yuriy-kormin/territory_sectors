from django.test import TestCase
from django.urls import reverse


class Create(TestCase):

    def test_create_open_without_login(self):
        response = self.client.get(reverse('flat_list'))
        self.assertEqual(response.status_code, 302)
