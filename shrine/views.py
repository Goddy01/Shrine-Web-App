from django.shortcuts import render
from events import models
from datetime import date

# Create your views here.
def home(request):
    events = models.Event.objects.filter(event_time__gte=date.today())
    return render(request, 'home.html', {'events': events})

def sermon(request):
    return render(request, 'sermons/sermons.html')

def donation(request):
    return render(request, 'donations/donations.html')