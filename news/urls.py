from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('add-news/', views.add_news, name='add_news'),
]