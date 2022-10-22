from .models import Donation, Donate
from django import forms

class AddDonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        exclude = ['donation_id', 'date_posted', 'amount_raised']

class DonateForm(forms.ModelForm):
    class Meta:
        model = Donate
        exclude = ('user', 'donated_id')

class UpdateDonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        exclude = ['donation_id', 'date_posted', 'amount_raised']