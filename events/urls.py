from django.urls import path
from . import views
app_name = 'events'

urlpatterns = [
    path('add-event/', views.add_event, name='add_event'),
    path('events/', views.event, name='event'),
]