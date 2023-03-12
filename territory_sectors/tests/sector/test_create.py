from django.test import TestCase
from django.urls import reverse, reverse_lazy


class Create(TestCase):

    def test_create_open_without_login(self):
        response = self.client.get(reverse('sector_list'))
        self.assertRedirects(response,
                             f'{reverse_lazy("user_login")}'
                             f'?next={reverse_lazy("sector_list")}')
