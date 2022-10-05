from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def sermon(request):
    return render(request, 'sermons/sermons.html')

def donation(request):
    return render(request, 'donations/donations.html')