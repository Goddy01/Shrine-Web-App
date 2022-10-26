from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import AddSermonForm, UpdateSermonForm
from .models import Sermon
from django.contrib import messages
from donations.models import Donation
import random, datetime
from datetime import date
from shrine.views import pagination
# Create your views here.

def sermons(request):
    """The view for rendering all the sermons on the sermon page"""
    sermons = Sermon.objects.all().order_by('sermon_date')
    past_sermons = Sermon.objects.filter(sermon_date__lte=date.today()).order_by('-sermon_date')[:2]
    upcoming_sermons = Sermon.objects.filter(sermon_date__gte=date.today())
    donations = Donation.objects.filter(complete=False)
    donations = list(donations)
    donation = random.choice(donations)
    
    # Using the Pagination template from shrine.views
    sermons_pag = pagination(request, upcoming_sermons, 3, 'sermon_date')
    return render(request, 'sermons/sermons.html', {'sermons':sermons, 'past_sermons': past_sermons, 'donation': donation, 'upcoming_sermons': upcoming_sermons, 'sermons_pag': sermons_pag})

def sermon_error_checker(request,sermon_form):
    """The view that checks for errors in sermon forms. Will be called when needed to abide by DRY"""
    if sermon_form.cleaned_data['sermon_date'] < datetime.datetime.now().date():
        messages.error(request, 'The sermon date cannot be in the past.')
    elif sermon_form.cleaned_data['sermon_date'] == datetime.datetime.now().date():
        messages.error(request, 'The sermon date cannot be today. The sermon must be posted atleast a day before the sermon date.')
    else:
        sermon_form = sermon_form.save(commit=False)
        sermon_form.sermon_priest_name = sermon_form.sermon_priest_name.title()
        sermon_form = sermon_form.save()

def add_sermon(request):
    """The view for adding sermons"""
    if request.user.is_admin:
        if request.method == 'POST':
            add_sermon_form = AddSermonForm(request.POST or None, request.FILES or None)
            if add_sermon_form.is_valid():
                sermon_error_checker(request, add_sermon_form)
                if add_sermon_form.cleaned_data['sermon_date'] > datetime.datetime.now().date():
                    return redirect('sermons:sermons')
            else:
                messages.error(request, 'The sermon could not be added.')
        else:
            add_sermon_form = AddSermonForm()
    else:
        return HttpResponse('You are not authorized to add sermons.')
    return render(request, 'sermons/add_Sermon.html', {'add_sermon_form': add_sermon_form})

def sermon_details(request, sermon_id):
    """The view that facilitates the display of ermon details"""
    sermon = Sermon.objects.get(sermon_id=sermon_id)
    return render(request, 'sermons/sermon_details.html', {'sermon':sermon})

def update_sermon(request, sermon_id):
    sermon = Sermon.objects.get(sermon_id=sermon_id)
    if request.user.is_admin:
        if request.method == 'POST':
            update_sermon_form = UpdateSermonForm(request.POST or None, request.FILES or None, instance=sermon)
            if update_sermon_form.is_valid():
                sermon_error_checker(request, update_sermon_form)
                if update_sermon_form.cleaned_data['sermon_date'] > datetime.datetime.now().date():
                    return redirect('sermons:sermons')
            else:
                messages.error(request, 'The sermon could not be updated.')
        else:
            update_sermon_form = UpdateSermonForm()
    else:
        return HttpResponse('Sorry. You are not authenticated to update the sermon.')
    update_sermon_form = UpdateSermonForm(instance=request.user, initial = {
                "sermon_title": sermon.sermon_title,
                "sermon_priest_name": sermon.sermon_priest_name,
                "sermon_date": sermon.sermon_date,
                "sermon_image": sermon.sermon_image,
                "sermon_desc": sermon.sermon_desc,
                "sermon_body": sermon.sermon_body,

        })
    return render(request, 'sermons/update_sermon.html', {'sermon': sermon, 'update_sermon_form': update_sermon_form})

def delete_sermon(request, sermon_id):
    if request.user.is_admin:
        sermon = Sermon.objects.get(sermon_id=sermon_id)
        sermon.delete()
        return redirect('sermons:sermons')
    return render(request, 'sermons/sermon_details.html')