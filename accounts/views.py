from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import UserRegForm

# Create your views here.

def user_reg_view(request):
    '''The view to register users'''
    if request.method == 'POST':
        reg_form = UserRegForm(request.POST)
        if reg_form.is_valid():
            user = reg_form.save()
            login(request, user) #Login users in after registration
            return redirect('home')
        else:
            messages.error(request, 'Registration Failed')
    else:
        reg_form = UserRegForm()
    return render(request, 'accounts/register.html', {'reg_form': reg_form})

