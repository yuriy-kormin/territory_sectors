import json
import os

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse, reverse_lazy

from territory_sectors.house.models import House

FIXTURE_DIR = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    'fixtures'
)


class Create(TestCase):
    def setUp(self):
        self.user_obj, _ = User.objects.get_or_create(username='testuser')
        fixture_file = os.path.join(FIXTURE_DIR, 'one_house.json')
        self.test_house = json.load(open(fixture_file))

    def test_create_open_without_login(self):
        response = self.client.get(reverse('house_list'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response,
                             f'{reverse_lazy("user_login")}'
                             f'?next={reverse_lazy("house_list")}')

    def test_open_create_with_login(self):
        self.client.force_login(user=self.user_obj)
        response = self.client.get(reverse('house_add'))
        self.assertEqual(response.status_code, 200)

    def test_post_create(self):
        self.client.force_login(user=self.user_obj)

        self.assertEqual(House.objects.all().count(), 0)
        self.client.get(reverse("house_add"))
        response = self.client.post(
            reverse('house_add'),
            self.test_house
        )
        self.assertRedirects(response, reverse('house_list'), 302,
                             fetch_redirect_response=True)
        self.assertEqual(House.objects.all().count(), 1)
        house = House.objects.first()
        self.test_house.pop('flats_data')
        for field, value in self.test_house.items():
            self.assertEqual(value, getattr(house, field))

    def test_bulk_flats_create(self):
        self.assertEqual(House.objects.all().count(), 0)
        self.client.force_login(user=self.user_obj)
