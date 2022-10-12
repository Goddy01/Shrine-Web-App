from django import forms
from .models import Sermon

class AddSermonForm(forms.ModelForm):
    sermon_image = forms.ImageField(widget=forms.FileInput, required=True)
    class Meta:
        model = Sermon
        exclude = ('sermon_id', 'slug')

class UpdateSermonForm(forms.ModelForm):
    sermon_image = forms.ImageField(widget=forms.FileInput, required=False)
    class Meta:
        model = Sermon
        exclude = ('sermon_id', 'slug')