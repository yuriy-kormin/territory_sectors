import json
import os
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse, reverse_lazy

from territory_sectors.house.models import House
from territory_sectors.language.models import Language

FIXTURE_DIR = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    'fixtures'
)


class CreatePage(TestCase):
    def test_create_open_without_login(self):
        response = self.client.get(reverse('house_list'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response,
                             f'{reverse_lazy("user_login")}'
                             f'?next={reverse_lazy("house_list")}')


class TestCreate(TestCase):
    def setUp(self):
        user_obj, _ = User.objects.get_or_create(username='testuser')
        fixture_file = os.path.join(FIXTURE_DIR, 'one_house.json')
        self.test_house = json.load(open(fixture_file))
        fixture_file = os.path.join(FIXTURE_DIR, 'one_flat.json')
        self.test_flat = json.load(open(fixture_file))
        self.lang = Language.objects.create(name='test_lang')
        self.client.force_login(user=user_obj)

    def test_open_create_with_login(self):
        response = self.client.get(reverse('house_add'))
        self.assertEqual(response.status_code, 200)

    def test_post_create(self):
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

    def test_house_with_flat_create(self):
        self.test_flat.update({"language": self.lang.id})
        self.test_house['flats_data'] = json.dumps(
            [self.test_flat]
        )
        response = self.client.post(
            reverse('house_add'),
            self.test_house
        )
        self.assertRedirects(response, reverse('house_list'), 302,
                             fetch_redirect_response=True)
        house = House.objects.first()
        flats = house.flat_set.all()
        self.assertEqual(flats.count(), 1)
        for field, value in self.test_flat.items():
            if field == "language":
                self.assertEqual(value, flats[0].language_id)
            else:
                self.assertEqual(value, str(getattr(flats[0], field)))

    def test_bulk_flats_create(self):
        self.test_flat.update({"language": self.lang.id})
        flats = []
        numbers = ['1', '4', '2', '-', '10']
        for flat_num in ",".join(numbers[:3]), numbers[3], numbers[4]:
            self.test_flat['number'] = flat_num
            flats.append(self.test_flat.copy())
        self.test_house['flats_data'] = json.dumps(flats)
        response = self.client.post(
            reverse('house_add'),
            self.test_house
        )
        self.assertRedirects(response, reverse('house_list'), 302,
                             fetch_redirect_response=True)
        house = House.objects.first()
        house_flats = house.flat_set.all()
        self.assertEqual(house_flats.count(), len(numbers))
        for number in numbers:
            flat_orm = house_flats.get(number=number)
            self.test_flat['number'] = number
            for field, value in self.test_flat.items():
                if field == "language":
                    self.assertEqual(value, flat_orm.language_id)
                else:
                    self.assertEqual(value, str(getattr(flat_orm, field)))
