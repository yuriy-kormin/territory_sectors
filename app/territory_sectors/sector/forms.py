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

    # status = forms.ModelChoiceField(queryset=Status.objects.all())
    class Meta:
        model = Sector
        fields = [
            'name',
            'uuid',
            'contour',
            'status',
            'for_search',
            'assigned_to',
        ]
        labels = {
            'name': _('Sector name'),
            'status': _('Sector status'),
            'for_search': _('for search'),
            'assigned_to': _('assigned to'),
        }
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': _('Please enter sector name')
                }
            ),
            'status': forms.Select(
                attrs={
                    'class': 'form-control',
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
            'contour': forms.HiddenInput(
                attrs={
                    'id': 'contour',
                },
            ),
        }

    # def clean_status(self):
    #     status_data = self.cleaned_data.get('status')
    #     return [status_data,]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
