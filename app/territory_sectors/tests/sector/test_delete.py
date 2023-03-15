from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse_lazy
from territory_sectors.sector.models import Sector


class Delete(TestCase):
    fixtures = ['territory_sectors/tests/sector/fixtures/one_sector.json']

    def setUp(self):
        self.user_obj, _ = User.objects.get_or_create(username='testuser')
        self.sector_obj = Sector.objects.first()
        self.path = reverse_lazy(
            'sector_delete', kwargs={'pk': self.sector_obj.pk})

    def test_open_delete_page(self):
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
