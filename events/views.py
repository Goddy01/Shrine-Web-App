from django.shortcuts import render
from django.http import HttpResponse
from .forms import EventForm
# Create your views here.

def event(request):
    return render(request, 'events/events.html')

def add_event(request):
    print(request.user.is_worshipper)
    if request.user.is_worshipper:
        if request.method == 'POST':
            event_form = EventForm(request.POST)
            if event_form.is_valid():
                event_form = event_form.save()
            else:
                event_form = EventForm()
        else:
            event_form = EventForm()
    else:
        return HttpResponse('You are not authorized to view this page.')
    return render(request, 'events/event_form.html', {'event_form': event_form})