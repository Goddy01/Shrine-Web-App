from django.urls import path
from . import views

app_name = 'sermons'

urlpatterns = [
    path('sermons/', views.sermons, name='sermons'),
    path('add-sermon/', views.add_sermon, name='add_sermon'),
    path('<sermon_id>/sermon_details/', views.sermon_details, name='sermon_details'),
    path('<sermon_id>/update_sermon/', views.update_sermon, name='update_sermon'),
    path('<sermon_id>/delete_sermon/', views.delete_sermon, name='delete_sermon'),
]
