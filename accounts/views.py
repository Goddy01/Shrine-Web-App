from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import UserRegForm, UserLoginForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def user_reg_view(request):
    '''The view that handles users registration'''
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

def user_login_view(request):
    '''The view that handles users login'''
    if request.method == 'POST':
        login_form = UserLoginForm(request.POST)
        if login_form.is_valid():
            email = request.POST.get('email')
            password = request.POST.get('password')
            user = authenticate(email=email, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('event')
            else:
                messages.error(request, 'User does not exist.')
        else:
            messages.error(request, 'Login Failed.')
    else:
        login_form = UserLoginForm()
    return render(request, 'accounts/login.html', {'login_form': login_form})

@login_required
def logout_view(request):
    '''The view that handles the loggin out of users'''
    logout(request)
    return redirect('home')