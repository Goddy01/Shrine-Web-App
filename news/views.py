from http.client import HTTPResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import AddNewsForm
from .models import News
# Create your views here.

def news(request):
    """The view for rendering all news on the news page"""
    news = News.objects.all().order_by('-date_posted')
    latest_news = News.objects.all().order_by('-date_posted')
    return render(request, 'news/news.html', {'news': news, 'latest_news': latest_news})

def add_news(request):
    """The view that facilitates the adding of news"""
    if request.user.is_staff:
        if request.method == 'POST':
            add_news_form = AddNewsForm(request.POST)
            if add_news_form.is_valid:
                add_news_form.save()
                return redirect('news:news')
            else:
                add_news_form = AddNewsForm()
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