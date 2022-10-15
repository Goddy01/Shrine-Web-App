from django.urls import path
from . import views

app_name = 'donations'

urlpatterns = [
    path('donations/', views.donations, name='donations'),
    path('add-donation/', views.add_donation, name='add_donation'),
]