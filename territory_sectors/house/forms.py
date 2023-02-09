from django import forms
from django.utils.translation import gettext_lazy as _
from .models import House
from territory_sectors.sector.models import Sector
from territory_sectors.uuid_qr.models import Uuid


class HouseForm(forms.ModelForm):
    class Meta:
        model = House
        # readonly_fields = ['gps_point', ]
        fields = [
            'address',
            'floor_amount',
            'entrances',
            # 'sector',
            # 'uuid',
            'gps_point',
            'desc',
            'id',
        ]
        widgets = {
            'address': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': _('Please enter address of building')
                }
            ),
            'floor_amount': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': _('Please set floors amount of building')
                }
            ),
            'entrances': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': _('How much entrances in building')
                }
            ),
            # 'sector': forms.Select(
            #     attrs={
            #         'class': 'form-control',
            #         'choices': Sector,
            #     }
            # ),
            'desc': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': _('Some description about house')
                }
            ),
            'gps_point': forms.HiddenInput(
                attrs={
                    'id': 'gps_point',
                },
            ),
        }
        # labels = {
        #     'name': _('Name'),
        # }
