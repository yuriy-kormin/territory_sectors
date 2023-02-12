from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Sector
from territory_sectors.uuid_qr.models import Uuid


class SectorForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(SectorForm, self).__init__(*args, **kwargs)
        # if self.is_bound: - этот метод определяет, это update или create
        # self.fields['uuid']
        self.fields['uuid'].queryset = Uuid.objects.filter(
            sector__isnull=True,
            house__isnull=True,
            flat__isnull=True,
        )

    class Meta:
        model = Sector
        fields = [
            'name',
            'uuid',
            'contour'
        ]
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': _('Please enter sector name')
                }
            ),
            # 'uuid': forms.Select(
            #     queryset=Uuid.objects.filter(
            #         sector__isnull=True,
            #         house__isnull=True,
            #         flat__isnull=True,
            #     ),
            #     # attrs={
            #     #     'class': 'form-control',
            #     #     'choices': Uuid,
            #     # }
            # ),
            'contour': forms.TextInput(
                attrs={
                    'id': 'contour',
                },
            ),
        }
