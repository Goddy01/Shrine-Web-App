from http.client import HTTPResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import AddNewsForm, UpdateNewsForm
from .models import News
from donations.models import Donation
import random
# Create your views here.

def news(request):
    """The view for rendering all news on the news page"""
    news = News.objects.all().order_by('-date_posted')
    latest_news = News.objects.all().order_by('-date_posted')
    donations = Donation.objects.filter(complete=False)
    donations = list(donations)
    donation = random.choice(donations)
    return render(request, 'news/news.html', {'news': news, 'latest_news': latest_news, 'donation': donation})

def add_news(request):
    """The view that facilitates the adding of news"""
    if request.user.is_staff:
        if request.method == 'POST':
            add_news_form = AddNewsForm(request.POST)
            if add_news_form.is_valid:
                add_news_form.save()
                return redirect('news:news')
            else:
                messages.error(request, 'Sorry the news could not be posted.')
        else:
            add_news_form = AddNewsForm()
    else:
        return HTTPResponse('Sorry. You are not authorized to post news.')
    return render(request, 'news/add_news.html', {'add_news_form': add_news_form})

def news_details(request, news_id):
    """The view that facilitates the display of news details"""
    news = News.objects.get(news_id=news_id)
    return render(request, 'news/news_details.html', {'news': news})

def update_news(request, news_id):
    """The view that facilitates the updating of new details"""
    news = News.objects.get(news_id=news_id)
    if request.user.is_staff:
        if request.method == 'POST':
            update_news_form = UpdateNewsForm(request.POST, instance=news)
            if update_news_form.is_valid:
                update_news_form.save()
                return redirect('news:news')
            else:
                messages.error(request, 'Sorry the news could not be updated.')
        else:
            update_news_form = UpdateNewsForm()
    else:
        return HTTPResponse('Sorry. You are not authorized to post news.')
    update_news_form = UpdateNewsForm(instance=request.user, initial = {
                            "news_headline": news.news_headline,
                            "news_body": news.news_body,
    }
    )
    return render(request, 'news/update_news.html', {'update_news_form': update_news_form, 'news': news})

def delete_news(request, news_id):
    """The view that facilitates the deletion of news"""
    if request.user.is_staff:
        news = News.objects.get(news_id=news_id)    
        news.delete()
        return redirect('news:news')
    return render(request, 'news/news_details.html')