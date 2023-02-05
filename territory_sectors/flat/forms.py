from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Flat
# from territory_sectors.sector.models import Sector
from territory_sectors.house.models import House
# from territory_sectors.uuid_qr.models import Uuid
from ..language.models import Language


class FlatForm(forms.ModelForm):
    class Meta:
        model = Flat
        # readonly_fields = ['gps_point', ]
        fields = [
            'house',
            'number',
            'entrance',
            'floor',
            'way_desc',
            'language',
            'id',
            'uuid',
        ]
        widgets = {
            'house': forms.Select(
                attrs={
                    'class': 'form-control',
                    'choices': House,
                    'onchange': 'flat_change_house(event)',
                }
            ),
            'number': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': _('If possible - set number. \
                    (use , as separator for multiply)')
                }
            ),
            'entrance': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': _('Please set entrance number')
                }
            ),
            'floor': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': _('Please set floor number')
                }
            ),
            'way_desc': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': _('Please describe flat place on floor'),
                    'rows': 5,
                }
            ),
            'language': forms.Select(
                attrs={
                    'class': 'form-control',
                    'choices': Language,
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
