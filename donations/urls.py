from django.urls import path
from . import views

app_name = 'donations'

urlpatterns = [
    path('donations/', views.donations, name='donations'),
    path('add-donation/', views.add_donation, name='add_donation'),
    path('<donation_id>/donation_details/', views.donation_details, name='donation_details'),
]