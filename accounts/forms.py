from django import forms
from .models import UserProfile
from django.contrib.auth.forms import UserCreationForm

class UserRegForm(UserCreationForm):
    '''Form for users registrtion'''
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'username', 'phone_number', 'country', 'email','password1', 'password2']
        # exclude = ('last_login', 'date_joined', 'is_admin', 'is_active', 'is_superuser', 'is_staff', 'is_worshipper')
        # fields = '__all__'

class UserLoginForm(forms.ModelForm):
    '''Form for users login'''
    class Meta:
        model = UserProfile
        fields = ('email', 'password')