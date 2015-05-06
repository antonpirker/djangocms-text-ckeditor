
from django import forms
from django.forms.models import ModelForm
from .models import StoryText


class TextForm(ModelForm):
    body = forms.CharField()

    class Meta:
        model = StoryText
        exclude = (
            'page',
            'position',
            'placeholder',
            'language',
            'plugin_type',
        )
