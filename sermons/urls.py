from django.urls import path
from . import views
app_name = 'sermons'

urlpatterns = [
    path('sermons/', views.sermons, name='sermons'),
    path('add-sermon/', views.add_sermon, name='add_sermon'),
    path('<sermon_id>/sermon_details/', views.sermon_details, name='sermon_details'),
]