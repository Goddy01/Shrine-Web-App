from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import AddDonationForm, DonateForm
from .models import Donation

# Create your views here.
def donations(request):
    donations = Donation.objects.all().order_by('-date_posted')
    return render(request, 'donations/donations.html', {'donations': donations})

def add_donation(request):
    if request.user.is_staff:
        if request.method == 'POST':
            add_donation_form = AddDonationForm(request.POST)
            if add_donation_form.is_valid():
                add_donation_form.save()
                return redirect('donations:donations')
            else:
                add_donation_form = AddDonationForm()
                messages.error(request, 'The donation could not be added.')
        else:
            add_donation_form = AddDonationForm()
    else:
        return HttpResponse('Sorry. You are not authenticated to add donations.')
    return render(request, 'donations/add_donation.html', {'add_donation_form': add_donation_form})

def donation_details(request, donation_id):
    donation = Donation.objects.get(donation_id=donation_id)
    return render(request, 'donations/donation_details.html', {'donation': donation})

def donate_temp(request, donation_id):
    donation = Donation.objects.get(donation_id=donation_id)
    return render(request, 'donations/donate.html', {'donation': donation})

def make_payment(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            donate_form = DonateForm(request.POST)
            if donate_form.is_valid():
                if donate_form.cleaned_data['bool'] != 'True':
                    donate_form = donate_form.save(commit=False)
                    donate_form.user = request.user
                    donate_form.save()
            else:
                donate_form = DonateForm()
                messages.error(request, 'Sorry. Your donation was not successful.')
        else:
            donate_form = DonateForm()
    else:
        return HttpResponse('Sorry, you need to be logged in before you can donate.')

    return render(request, 'donations/donate.html')