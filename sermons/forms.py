from django import forms
from .models import Sermon

class AddSermonForm(forms.ModelForm):
    class Meta:
        model = Sermon
        exclude = ('sermon_id', 'slug')

class UpdateSermonForm(forms.ModelForm):
    class Meta:
        model = Sermon
        exclude = ('sermon_id', 'slug')