from .models import Donation, Donate
from django import forms

class AddDonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        exclude = ['donation_id', 'date_posted']

class DonateForm(forms.ModelForm):
    class Meta:
        model = Donate
        fields = '__all__'