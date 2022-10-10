from django.urls import path
from . import views
app_name = 'sermons'

urlpatterns = [
    path('add-sermon/', views.add_sermon, name='add_sermon'),
]