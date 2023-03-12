import json
import os
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse_lazy
from territory_sectors.house.models import House

FIXTURE_DIR = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    'fixtures'
)


class OpenWithoutLogin(TestCase):
    fixtures = ['territory_sectors/tests/fixtures/house_without_flats.json']

    def test_open_update_page(self):
        house = House.objects.first()
        response = self.client.get(
            reverse_lazy('house_update', kwargs={'pk': house.pk})
        )
        self.assertRedirects(
            response,
            f'{reverse_lazy("user_login")}'
            f'?next={reverse_lazy("house_update", kwargs={"pk": house.pk})}',
            302,
            fetch_redirect_response=True
         )


class TestUpdate(TestCase):
    def setUp(self):
        user_obj, _ = User.objects.get_or_create(username='testuser')
        fixture_file = os.path.join(FIXTURE_DIR, 'one_house.json')
        self.fixture_house = json.load(open(fixture_file))
        self.fixture_house.pop('flats_data')
        self.test_house = House.objects.create(**self.fixture_house)
        self.client.force_login(user=user_obj)

    def test_update(self):
        house = House.objects.first()
        response = self.client.get(
            reverse_lazy('house_update', kwargs={'pk': house.pk})
        )
        self.assertEqual(response.status_code, 200)
        response = self.client.post(
            reverse_lazy('house_update', kwargs={'pk': house.pk}),
            self.fixture_house
        )
        self.assertEqual(response.status_code, 200)
        house = House.objects.first()
        for field, value in self.fixture_house.items():
            self.assertEqual(getattr(house, field), value)
