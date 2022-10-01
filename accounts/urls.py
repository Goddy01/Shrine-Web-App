from django.urls import path
from . import views
app_name = 'accounts'

urlpatterns = [
    path('sign-up/', views.user_reg_view, name='reg'),
]