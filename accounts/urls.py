from django.urls import path
from . import views
app_name = 'accounts'

urlpatterns = [
    path('sign-up/', views.user_reg_view, name='reg'),
    path('sign-in/', views.user_login_view, name='login'),
    path('sign-out/', views.logout_view, name='logout'),
]