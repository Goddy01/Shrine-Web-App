from django import forms
from .models import News

class AddNewsForm(forms.ModelForm):
    class Meta:
        model = News
        exclude = ('news_id', 'date_posted')

class UpdateNewsForm(forms.ModelForm):
    class Meta:
        model = News
        exclude = ('news_id', 'date_posted')