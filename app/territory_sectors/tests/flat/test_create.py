from django.test import TestCase
from django.urls import reverse_lazy
from django.contrib.auth.models import User


class CreateFlat(TestCase):
    # fixtures = ['one_flat.json']
    def setUp(self):
        # with open(os.path.join('fixtures', 'one_flat.json')) as fixture:
        #     self.test_task = json.load(fixture)
        self.user_obj = User.objects.get_or_create(username='testuser')

    def test_create_open_without_login(self):
        response = self.client.get(reverse_lazy('flat_add'))
        self.assertRedirects(response,
                             f'{reverse_lazy("user_login")}'
                             f'?next={reverse_lazy("flat_add")}')

    def test_login_create(self):
        pass

    # def test_create_same(self):
    #     self.client.force_login(self.user_obj[0])
    #     f = Flat.objects.first()
        # response = self.client.post(path=reverse_lazy('flat_add'),
        #                             data=f)
        # self.assertRedirects
