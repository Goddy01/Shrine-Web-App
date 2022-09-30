from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def events(request):
    return render(request, 'events/events.html')