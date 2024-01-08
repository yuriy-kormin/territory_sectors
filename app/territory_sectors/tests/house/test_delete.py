from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse_lazy

from territory_sectors.flat.models import Flat
from territory_sectors.house.models import House


class Delete(TestCase):
    fixtures = ['territory_sectors/tests/fixtures/house_without_flats.json']

    def test_open_delete_page_without_login(self):
        house = House.objects.first()
        response = self.client.get(
            reverse_lazy('house_delete', kwargs={'pk': house.pk})
        )
        self.assertRedirects(
            response,
            f'{reverse_lazy("user_login")}'
            f'?next={reverse_lazy("house_delete", kwargs={"pk": house.pk})}',
            302,
            fetch_redirect_response=True
        )

    def test_remove_house(self):
        user_obj, _ = User.objects.get_or_create(username='testuser')
        self.client.force_login(user=user_obj)
        self.assertEqual(House.objects.all().count(), 1)
        house = House.objects.first()
        self.client.post(
            reverse_lazy('house_delete', kwargs={'pk': house.pk})
        )
        self.assertEqual(House.objects.all().count(), 0)


class TestRemoveRelatedFlats(TestCase):
    fixtures = ['territory_sectors/tests/fixtures/house_with_flats.json']

    def test_related(self):
        user_obj, _ = User.objects.get_or_create(username='testuser')
        self.client.force_login(user=user_obj)
        self.assertEqual(House.objects.all().count(), 1)
        house = House.objects.first()
        self.assertEqual(house.flat_set.all().count(), 2)
        response = self.client.post(
            reverse_lazy('house_delete', kwargs={'pk': house.pk})
        )
        self.assertRedirects(response,
                             f'{reverse_lazy("sector_list")}')
        self.assertEqual(House.objects.all().count(), 0)
        self.assertEqual(Flat.objects.all().count(), 0)
