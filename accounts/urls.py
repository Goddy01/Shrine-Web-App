from django.urls import path, reverse_lazy, include
from django.contrib.auth import views as auth_views
from . import views
app_name = 'accounts'

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('sign-up/', views.user_reg_view, name='reg'),
    path('sign-in/', views.user_login_view, name='login'),
    path('sign-out/', views.logout_view, name='logout'),

    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name="accounts/password/password_change_done.html"), name="password_change_done"),

    path('password_reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password/password_reset_done.html"), name="password_reset_done"),

    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password/password_reset_complete.html'), name="password_reset_complete"),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='accounts/password/password_reset_form.html', 
        success_url = reverse_lazy('password_reset_complete'),
    ), name="password_reset_confirm"),

    path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name='accounts/password/password_reset.html',
        email_template_name='accounts/password/password_reset_email.html',
        subject_template_name='accounts/password/password_reset_subject.txt',
        success_url = reverse_lazy('password_reset_done'),
    ), name='password_reset'),
]