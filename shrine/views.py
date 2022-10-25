from django.shortcuts import render
from news.models import News
from events.models import Event
from donations.models import Donation
from sermons.models import Sermon
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
def home(request):
    news = News.objects.all().order_by('-date_posted')[:3]
    events = Event.objects.all().order_by('-event_date')[:3]
    donations = Donation.objects.filter(complete=False)[:3]
    sermons = Sermon.objects.all().order_by('-sermon_date')[:3]
    return render(request, 'home.html', {'news': news, 'events': events, 'donations': donations, 'sermons': sermons})

def pagination(request, items_list, num_of_pages, object_id):
    page_number = request.GET.get('page', 1)
    objects_paginator = Paginator(items_list.order_by(f'-{object_id}'), num_of_pages)
    try:
        objects = objects_paginator.page(page_number)
    except PageNotAnInteger:
        objects = objects_paginator.page(1)
    except EmptyPage:
        objects = objects_paginator.page(objects_paginator.num_pages)
    return objects