from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import AddDonationForm, DonateForm, UpdateDonationForm
from .models import Donation
from shrine.views import pagination

# Create your views here.
def donations(request):
    donations = Donation.objects.filter(complete=False).order_by('-date_posted')
    completed_donations = Donation.objects.filter(complete=True).order_by('-date_posted')[:3]
    donations_pag = pagination(request, donations, 3, 'amount_needed')
    return render(request, 'donations/donations.html', {'donations': donations, 'completed_donations': completed_donations, 'donations_pag': donations_pag})

def add_donation(request):
    if request.user.is_admin:
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
        if request.method == 'POST':
            donate_form = DonateForm(request.POST)
            if donate_form.is_valid():
                if request.POST.get('bool') == 'True':
                    donate_form = donate_form.save(commit=False)
                    donate_form.user = request.user
                    donate_form.save()
                    if donation.amount_raised is not None:
                        donation.amount_raised += donate_form.amount_donated
                    else:
                        donation.amount_raised = donate_form.amount_donated
                    donation.amount_needed -= donate_form.amount_donated
                    if donation.amount_needed == 0:
                        donation.complete = not donation.complete
                    donation.save()
                    messages.success(request, 'Thank you for your donation. (Arigato!)')
                    # return render(request, 'donations/donation_details.html')
                    return redirect('/donations/donations/')
            else:
                # donate_form = DonateForm()
                messages.error(request, 'Sorry. Your donation was not successful.')
        else:
            donate_form = DonateForm()
        context['donate_form'] = donate_form
    else:
        return HttpResponse('Sorry, you need to be logged in before you can donate.')

    return render(request, 'donations/donate.html', context)

def update_donation(request, donation_id):
    donation = Donation.objects.get(donation_id=donation_id)
    if request.user.is_admin:
        if request.method == 'POST':
            update_donation_form = UpdateDonationForm(request.POST, instance=donation)
            if update_donation_form.is_valid():
                update_donation_form.save()
                return redirect('donations:donations')
            else:
                messages.error(request, 'The donation could not be updated.')
        else:
            update_donation_form = UpdateDonationForm()
    else:
        return HttpResponse('You are not authenticated to update donations.')
    # update_donation_form = UpdateDonationForm(instance=request.user, initial = {
    #     "donation_name": donation.donation_name,
    #     "donation_desc": donation.donation_desc,
    #     "amount_needed": donation.amount_needed,
    # })
    return render(request, 'donations/update_donation.html', {'update_donation_form': update_donation_form, 'donation': donation})

def delete_donation(request, donation_id):
    if request.user.admin:
        donation = Donation.objects.get(donation_id=donation_id)
        donation.delete()
        return redirect('donations:donations')
    return render(request, 'donations/donation_details.html')