from django.shortcuts import render
from news.models import News
from events.models import Event
from donations.models import Donation
# Create your views here.
def home(request):
    news = News.objects.all().order_by('-date_posted')[:3]
    events = Event.objects.all().order_by('event_date')[:3]
    donations = Donation.objects.filter(complete=False)[:3]
    sermons = Sermon.objects.all().order_by('-sermon_date')[:3]
    return render(request, 'home.html', {'news': news, 'events': events, 'donations': donations, 'sermons': sermons})