from django import forms
from . import models
from django.contrib.auth.forms import UserCreationForm

class UserRegForm(UserCreationForm):
    class Meta:
        model = models.UserProfile
        fields = '__all__'