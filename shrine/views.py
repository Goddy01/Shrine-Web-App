from django.http import HttpResponse
from django.shortcuts import render
from news.models import News
from events.models import Event
from donations.models import Donation
from sermons.models import Sermon
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import date
from itertools import chain
from django.db.models import Q

# Create your views here.
def home(request):
    """The view for rendering info on the home page"""
    news = News.objects.all().order_by('-date_posted')[:3]
    events = Event.objects.filter(event_date__gte=date.today()).order_by('event_date')[:3]
    donations = Donation.objects.filter(complete=False)[:3]
    sermons = Sermon.objects.filter(sermon_date__gte=date.today()).order_by('sermon_date')[:3]
    return render(request, 'home.html', {'news': news, 'events': events, 'donations': donations, 'sermons': sermons})

def pagination(request, items_list, num_of_pages, object_id):
    """Pagination template. Created for easy pagination and to abide by DRY"""
    page_number = request.GET.get('page', 1)
    objects_paginator = Paginator(items_list.order_by(f'{object_id}'), num_of_pages)
    try:
        objects = objects_paginator.page(page_number)
    except PageNotAnInteger:
        objects = objects_paginator.page(1)
    except EmptyPage:
        objects = objects_paginator.page(objects_paginator.num_pages)
    return objects

def search(request):
    """The view that performs the search functionality"""
    context = {}
    if request.method == 'GET':
        query = request.GET.get('query', '')
        if query is not None:
            news = News.objects.filter(Q(news_headline__icontains=query)).distinct()
            sermons = Sermon.objects.filter(Q(sermon_title__icontains=query)).distinct()
            donations = Donation.objects.filter(Q(donation_name__icontains=query)).distinct()
            events = Event.objects.filter(Q(event_name__icontains=query)).distinct()

            if not news and not sermons and not donations and not events:
                return HttpResponse('Your search returned no result.')
            
            results = chain(news, sermons, donations, events)
            # results_pag = pagination(request, results, 4, )
            context['results'] = results
            context['query'] = str(query)
            return render(request, 'home.html', context)
        else:
            return render(request, 'home.html')
    else:
        return render(request, 'home.html')