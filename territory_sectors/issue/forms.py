from django import forms
from django.contrib.auth.models import User
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

    # def __init__(self, *args, **kwargs):
    #     # self.is_create = kwargs.get('instance') is None
    #     super().__init__(*args, **kwargs)
    #     # if not self.is_create:
    #     self.fields['new_comment'].initial = ''
    #     # else:
    #     #     self.fields['flats_data'].initial = '[]'
    #
    # def clean_new_comment(self):
    #     comment = self.cleaned_data.get('new_comment')
    #     if not len(comment):
    #         raise forms.ValidationError("Invalid JSON data.")
    #     return comment
    #
    # def save(self):
    #     Comment.objects.create(
    #         author_id=self.request.user.id,
    #         issue_id=self.instance.id,
    #         text=self.cleaned_data.get('text')
    #     )
    #     return self.instance
