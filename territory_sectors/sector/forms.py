from django import forms
from django.db.models import Q
from django.utils.translation import gettext_lazy as _
from .models import Sector
from territory_sectors.uuid_qr.models import Uuid


class SectorForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.is_create = kwargs.get('instance') is None
        super(SectorForm, self).__init__(*args, **kwargs)
        # if self.is_bound: - этот метод определяет, это update или create
        # self.fields['uuid']
        if self.is_create:
            self.fields['uuid'].queryset = Uuid.objects.filter(
                sector__isnull=True,
                house__isnull=True,
                flat__isnull=True,
            )
        else:
            self.fields['uuid'].queryset = Uuid.objects.filter(
                Q(
                    sector__isnull=True,
                    house__isnull=True,
                    flat__isnull=True,
                ) | Q(
                    id=kwargs['instance'].uuid
                )
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
