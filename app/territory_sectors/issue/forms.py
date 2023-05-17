from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Issue, Comment


class IssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = [
            'title',
            'text',
        ]
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': _('Please enter issue name')
                }
            ),
            'text': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': _('Please enter issue text'),
                    'rows': 5,
                },
            ),
        }


class CommentForm(forms.ModelForm):
    completed = forms.BooleanField(
        initial=False,
        label=_('Task is completed'),
        required=False,
    )

    class Meta:
        model = Comment
        fields = ('text',)
        widgets = {
            'text': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': _('Enter your comment here'),
                    'rows': 5,

                }
            ),
        }
        labels = {'text': _('Reply')}

    def save(self, commit=True):
        if self.cleaned_data.get('text'):
            return super().save(self)
        return super().save(commit=False)
