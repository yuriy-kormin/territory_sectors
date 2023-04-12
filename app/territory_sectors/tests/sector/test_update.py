from django.contrib.auth.models import User
from django.db.models import DateTimeField
from django.test import TestCase
from django.urls import reverse_lazy

from territory_sectors.sector.models import Sector
from territory_sectors.sector.forms import SectorForm


class Update(TestCase):
    fixtures = ['territory_sectors/tests/sector/fixtures/one_sector.json']

    def setUp(self):
        self.user_obj, _ = User.objects.get_or_create(username='testuser')
        self.sector_obj = Sector.objects.first()
        self.path = reverse_lazy(
            'sector_update', kwargs={'pk': self.sector_obj.pk})

    def test_open_update_page(self):
        response = self.client.get(self.path)
        self.assertRedirects(
            response,
            f'{reverse_lazy("user_login")}'
            f'?next={self.path}',
            302,
            fetch_redirect_response=True
        )

    def test_open_login(self):
        self.client.force_login(user=self.user_obj)
        response = self.client.get(self.path)
        self.assertEqual(response.status_code, 200)

    def test_same_uuid_after_update(self):
        def compare_instances(inst1, inst2):
            return all([
                getattr(inst1, attr.name) == getattr(inst2, attr.name)
                for attr in inst1._meta.get_fields()
                if not isinstance(attr, DateTimeField)
                ])

        self.client.force_login(user=self.user_obj)
        modified_sector = self.sector_obj
        modified_sector.name = 'something_for test&^5'
        modified_sector.assigned_to = 'test assignments'
        modified_sector.for_search = not modified_sector.for_search
        response = self.client.post(self.path, {
            field: getattr(modified_sector, field) for
            field in SectorForm.Meta.fields
        })
        self.assertEqual(response.status_code, 200)
        self.sector_obj.refresh_from_db()
        self.assertTrue(
            compare_instances(
                self.sector_obj,
                modified_sector
            )
        )
