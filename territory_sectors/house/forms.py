import json

from django import forms
# from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from .models import House
from territory_sectors.flat.models import Flat


class HouseForm(forms.ModelForm):
    flats_data = forms.CharField()

    #
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
            'flats_data',
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
            'desc': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': _('Some description about house')
                }
            ),
            'gps_point': forms.HiddenInput(
                # error_messages={
                #     'required': "Please Enter gps"},
                attrs={
                    'id': 'gps_point',
                },
            ),
            'flats_data': forms.HiddenInput(
                attrs={
                    'class': 'form-control',
                    'id': 'flats_data',
                }
            )
        }

    def __init__(self, *args, **kwargs):
        self.is_create = kwargs.get('instance') is None
        super().__init__(*args, **kwargs)
        # instance = self.instance
        if not self.is_create:
            self.fields['flats_data'].initial = self.instance.flats_json()

    def clean_flats_data(self):
        flats_data = self.cleaned_data.get('flats_data')
        # try:
        #     hidden_field = json.loads(hidden_field)
        # except json.JSONDecodeError:
        #     raise forms.ValidationError("Invalid JSON data.")
        return flats_data

    def save(self):
        obj = super().save()
        flats_data = json.loads(self.cleaned_data.get('flats_data'))
        instances = []
        for flat in flats_data:
            if 'id' not in flat.keys():
                instance = Flat.objects.create(house=obj)
            else:
                instance = Flat.objects.get(id=flat['id'])
            instance.entrance = flat['entrance']
            instance.floor = flat['floor']
            instance.number = flat['number']
            instance.way_desc = flat['way_desc']
            instance.save()
            #     instance.key = flat[key]
            instances.append(instance)
        #     # fields.append(key)
        # raise IOError(instances)
        # Flat.objects.abulk_update(instances,
        #                           ['entrance', 'floor',
        #                           'number', 'way_desc'])
        return obj
