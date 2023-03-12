from django.test import TestCase
from territory_sectors.house.models import House
from territory_sectors.language.models import Language


class Delete(TestCase):
    fixtures = ['territory_sectors/tests/fixtures/house_with_flats.json']

    def setUp(self):
        self.house = House.objects.first()

    def test_get_ru_flats(self):
        ru_flats = self.house.get_ru_flats()
        self.assertEqual(ru_flats.count(), 1)
        self.assertEqual(ru_flats[0].pk, 24)

    def test_get_flat_count(self):
        self.assertEqual(self.house.flat_count(), 2)

    def test_get_lang_list(self):
        self.assertEqual(
            list(Language.objects.all()),
            list(self.house.get_lang_list_qs())
        )
