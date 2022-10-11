from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import AddSermonForm, UpdateSermonForm
from .models import Sermon
from django.contrib import messages
import datetime
# Create your views here.

def sermons(request):
    sermons = Sermon.objects.all().order_by('sermon_date')
    return render(request, 'sermons/sermons.html', {'sermons':sermons})

def sermon_error_checker(request,sermon_form):
    """A view that checks for errors in sermon forms. Will be called when needed to abide by DRY"""
    if sermon_form.cleaned_data['sermon_date'] < datetime.datetime.now().date():
        messages.error(request, 'The sermon date cannot be in the past.')
    elif sermon_form.cleaned_data['sermon_date'] == datetime.datetime.now().date():
        messages.error(request, 'The sermon date cannot be today. The sermon must be posted atleast a day before the sermon date.')
    else:
        sermon_form = sermon_form.save(commit=False)
        sermon_form.sermon_location = sermon_form.sermon_location.title()
        sermon_form = sermon_form.save()

def add_sermon(request):
    if request.user.is_staff:
        if request.method == 'POST':
            add_sermon_form = AddSermonForm(request.POST or None, request.FILES or None)
            if add_sermon_form.is_valid():
                sermon_error_checker(request, add_sermon_form)
                if add_sermon_form.cleaned_data['sermon_date'] > datetime.datetime.now().date():
                    return redirect('sermons:sermon')
            else:
                add_sermon_form = AddSermonForm()
                messages.error(request, 'The sermon could not be added.')
        else:
            add_sermon_form = AddSermonForm()
    else:
        return HttpResponse('You are not authorized to add sermons.')
    return render(request, 'sermons/add_Sermon.html', {'add_sermon_form': add_sermon_form})