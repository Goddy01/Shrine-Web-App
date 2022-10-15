from .models import Donation
from django import forms

class AddDonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        exclude = ['donation_id', 'date_posted']