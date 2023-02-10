from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from .models import Flat
# from territory_sectors.sector.models import Sector
from territory_sectors.house.models import House
# from territory_sectors.uuid_qr.models import Uuid
from ..language.models import Language


class FlatForm(forms.ModelForm):
    class Meta:
        model = Flat
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
                    'placeholder': _('Please set number, if possible. Elsewhere - stay it empty. \
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

    def clean_number(self):
        number = self.cleaned_data.get('number', None)
        if number is None:
            return number
        house = self.cleaned_data.get('house', None)
        same_object = Flat.objects.filter(house=house, number=number)
        if self.instance:
            same_object = same_object.exclude(id=self.instance.id)
        if same_object.exists():
            raise ValidationError(
                'Database contains this flat number. Please set another')
        return number
