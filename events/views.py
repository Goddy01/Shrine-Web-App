from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import EventForm
# Create your views here.

def event(request):
    return render(request, 'events/events.html')

def add_event(request):
    print(request.user.is_worshipper)
    if request.user.is_staff:
        if request.method == 'POST':
            event_form = EventForm(request.POST)
            if event_form.is_valid():
                event_form = event_form.save()
                # messages.success(request, 'The event has been added successfully.')
                return redirect('events:event')
            else:
                event_form = EventForm()
                messages.error(request, 'The event could not be added.')
        else:
            event_form = EventForm()
    else:
        return HttpResponse('You are not authorized to view this page.')
    return render(request, 'events/event_form.html', {'event_form': event_form})