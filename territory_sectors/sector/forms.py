from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Sector
from territory_sectors.uuid_qr.models import Uuid


class SectorForm(forms.ModelForm):

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

    def __init__(self, *args, **kwargs):
        super(SectorForm, self).__init__(*args, **kwargs)
        # self.fields['uuid'].queryset =
        self.fields['uuid'] = forms.ModelChoiceField(
            queryset=Uuid.objects.filter(
                    sector__isnull=True,
                    house__isnull=True,
                    flat__isnull=True,
                ),
            widget=forms.Select(
                attrs={'class': 'form-control'}
            )
        )
