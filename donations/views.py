from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import AddDonationForm
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