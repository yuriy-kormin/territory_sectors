from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Status


class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ['name']

        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': _('Please enter status name')
                }
            ),
        }
