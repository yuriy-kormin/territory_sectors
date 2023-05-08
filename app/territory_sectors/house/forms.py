import json

from django import forms
from django.utils.translation import gettext_lazy as _
from .models import House
from territory_sectors.flat.models import Flat


class HouseForm(forms.ModelForm):
    flats_data = forms.CharField(widget=forms.HiddenInput)

    class Meta:
        model = House
        fields = [
            'image_preview',
            'image',
            'address',
            'floor_amount',
            'entrances',
            'for_search',
            'gps_point',
            'desc',
            'tech_desc',
            'id',
            # 'flats_data',
        ]
        labels = {
            'address': _('Address'),
            'floor_amount': _('Floors amount'),
            'entrances': _('Entrances amount'),
            'for_search': _('for_search'),
            'desc': _('Desc to find house'),
            'name': _('Tech desc'),
            'image': _('image')
        }
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
            'for_search': forms.CheckboxInput(
                attrs={
                    'class': 'form-check-input',
                }
            ),
            'desc': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': _('Description HOW TO FIND house('
                                     ' will be seen on sector print)'),
                    'rows': 2,
                    'style': "white-space: pre-wrap;"
                }
            ),
            'tech_desc': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': _('Technical description. Can see'
                                     ' only by logged in users'),
                    'rows': 2,
                    'style': "white-space: pre-wrap;"
                }
            ),
            'gps_point': forms.HiddenInput(
                # error_messages={
                #     'required': "Please Enter gps"},
                attrs={
                    'id': 'gps_point',
                },
            ),
        }

    def __init__(self, *args, **kwargs):
        self.is_create = kwargs.get('instance') is None
        super().__init__(*args, **kwargs)
        # instance = self.instance
        if not self.is_create:
            self.fields['flats_data'].initial = self.instance.flats_json()
        else:
            self.fields['flats_data'].initial = '[]'

    def clean_flats_data(self):
        flats_data = self.cleaned_data.get('flats_data')
        # try:
        #     hidden_field = json.loads(hidden_field)
        # except json.JSONDecodeError:
        #     raise forms.ValidationError("Invalid JSON data.")
        return flats_data

    def save(self):
        def instance_set_data(instance, data):
            for key in data:
                if key == 'id':
                    continue
                key_name = key + '_id' if key == 'language' else key
                setattr(instance, key_name, data[key])

        obj = super().save()
        if not self.cleaned_data.get('image'):
            obj.image_preview.delete()
            obj.save()
        flats = self.cleaned_data.get('flats_data')
        if flats:
            flats_data = json.loads(flats)
            instances = []
            for flat in flats_data:
                if 'id' not in flat.keys():
                    # its a create flat action
                    for flat_number in flat['number'].split(','):
                        flat_set = flat.copy()
                        flat_set['number'] = flat_number
                        instance = Flat.objects.create(house=obj)
                        instance_set_data(instance, flat_set)
                        instance.save()
                else:
                    # here is a modify flat action
                    if flat['id'].find("*remove") != -1:
                        flat_id = int(flat['id'].split("*")[0])
                        Flat.objects.get(id=flat_id).delete()
                        continue
                    instance = Flat.objects.get(id=int(flat['id']))
                    for i, flat_number in enumerate(flat['number'].split(',')):
                        if i == 0:
                            flat_set = flat.copy()
                            flat_set['number'] = flat_number
                            instance_set_data(instance, flat_set)
                            instance.save()
                        else:
                            flat_set = flat.copy()
                            flat_set['number'] = flat_number
                            instance = Flat.objects.create(house=obj)
                            instance_set_data(instance, flat_set)
                            instance.save()
                instances.append(instance)
        return obj
