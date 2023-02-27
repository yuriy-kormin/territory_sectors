from django import forms
from django.utils.translation import gettext_lazy as _
from ..models import StatusSector


class SectorForm(forms.ModelForm):
    class Meta:
        model = StatusSector
        fields = [
            'name',
            'uuid',
            'contour',
            'status',
        ]
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': _('Please enter sector name')
                }
            ),
            'contour': forms.HiddenInput(
                attrs={
                    'id': 'contour',
                },
            ),
        }

