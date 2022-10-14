from http.client import HTTPResponse
from django.shortcuts import render
from django.contrib import messages
from .forms import AddNewsForm
# Create your views here.

def add_news(request):
    if request.user.is_staff:
        if request.method == 'POST':
            add_news_form = AddNewsForm(request.POST)
            if add_news_form.is_valid:
                add_news_form.save()
            else:
                add_news_form = AddNewsForm()
                messages.error(request, 'Sorry the news could not be posted.')
        else:
            add_news_form = AddNewsForm()
    else:
        return HTTPResponse('Sorry. You are not authorized to post news.')
    return render(request, 'news/add_news.html')