from django import forms
from .models import UserProfile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

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
        fields = ['email', 'password']

    def clean(self):
        '''Customized the clean function to throw an error for invalid login details'''
        if self.is_valid():
            email = self.cleaned_data.get('email')
            password = self.cleaned_data.get('password')
            user = authenticate(email=email, password=password)

            if not user:
                # Throws a ValidationError in the form
                raise forms.ValidationError("User does not exist.")
