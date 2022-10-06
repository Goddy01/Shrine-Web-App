from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import EventForm, UpdateEventForm
import datetime
from .models import Event
# Create your views here.

def event(request):
    events = Event.objects.all().order_by('event_date')
    return render(request, 'events/events.html', {'events': events})

def event_error_checker(request,event_form):
    """A view that checks for errors in event forms. Will be called when needed to abide by DRY"""
    if event_form.cleaned_data['event_date'] < datetime.datetime.now().date():
        messages.error(request, 'The event date cannot be in the past.')
    elif event_form.cleaned_data['event_date'] == datetime.datetime.now().date():
        messages.error(request, 'The event date cannot be today. The event must be posted atleast a day before the event date.')
    else:
        event_form = event_form.save(commit=False)
        event_form.event_location = event_form.event_location.title()
        event_form = event_form.save()
        # messages.success(request, 'The event has been added successfully.')
        return redirect('events:event')

def add_event(request):
    print(request.user.is_worshipper)
    if request.user.is_staff:
        if request.method == 'POST':
            event_form = EventForm(request.POST)
            if event_form.is_valid():
                event_error_checker(request, event_form)
            else:
                event_form = EventForm()
                messages.error(request, 'The event could not be added.')
        else:
            event_form = EventForm()
    else:
        return HttpResponse('You are not authorized to view this page.')
    return render(request, 'events/event_form.html', {'event_form': event_form})

def event_detail(request, event_id):
    event = Event.objects.get(event_id=event_id)
    return render(request, 'events/event_details.html', {'event': event})

def update_event(request, event_id):
    """The view to modify/update previously posted events."""
    event = Event.objects.get(event_id=event_id)
    if request.user.is_staff:
        if request.method == 'POST':
            update_event_form = UpdateEventForm(request.POST, instance=event)
            if update_event_form.is_valid():
                event_error_checker(request, update_event_form)
            else:
                update_event_form = UpdateEventForm()
                messages.error(request, 'The event could not be updated.')
        else:
        event_form = UpdateEventForm()
    else:
        return HttpResponse('You are not authorized to view this page.')
    return HttpResponse('Updated.')