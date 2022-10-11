from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import AddSermonForm, UpdateSermonForm
from django.contrib import messages
# Create your views here.

def add_sermon(request):
    if request.user.is_staff:
        if request.method == 'POST':
            add_sermon_form = AddSermonForm(request.POST or None, request.FILES or None)
            if add_sermon_form.is_valid():
                add_sermon_form = add_sermon_form.save(commit=False)
                if add_sermon_form.is_past_due():
                    messages.error(request, 'The date of the sermon cannot be in the past.')
                add_sermon_form.save()
                return redirect('home')
            else:
                add_sermon_form = AddSermonForm()
                messages.error(request, 'The sermon could not be added.')
        else:
            add_sermon_form = AddSermonForm()
    else:
        return HttpResponse('You are not authorized to add sermons.')
    return render(request, 'sermons/add_Sermon.html', {'add_sermon_form': add_sermon_form})