from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('news/', views.news, name='news'),
    path('add-news/', views.add_news, name='add_news'),
    path('<news_id>/news_details/', views.news_details, name='news_details'),
]