from django.urls import path
from . import views
app_name = 'events'

urlpatterns = [
    path('add-event/', views.add_event, name='add_event'),
    path('events/', views.event, name='event'),
    path('<event_id>/event_detail/', views.event_detail, name='event_detail'),
    path('<event_id>/update_event/', views.update_event, name='update_event'),
]