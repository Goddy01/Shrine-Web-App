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
                # add_donation_form = AddDonationForm()
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

def make_payment(request, donation_id):
    if request.user.is_authenticated:
        context = {}
        donation = Donation.objects.get(donation_id=donation_id)
        context['donation'] = donation
        print('BRUVVV')
        if request.method == 'POST':
            print('POSTED')
            donate_form = DonateForm(request.POST)
            # print(donate_form)
            if donate_form.is_valid():
                print('SHIT IS VALID')
                if request.POST.get('bool') == 'True':
                    donate_form = donate_form.save(commit=False)
                    donate_form.user = request.user
                    print('HERE: ', donate_form.user)
                    donate_form.save()
                    # messages.success(request, 'BRO')
                    return redirect('donations:donations')
            else:
                # donate_form = DonateForm()
                messages.error(request, 'Sorry. Your donation was not successful.')
        else:
            donate_form = DonateForm()
        context['donate_form'] = donate_form
    else:
        return HttpResponse('Sorry, you need to be logged in before you can donate.')

    return render(request, 'donations/donate.html', context)