from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import EventForm, UpdateEventForm, QuestionForm, AnswerForm
import datetime
from .models import Event, Question, Answer
from accounts.models import UserProfile
# Create your views here.

def event(request):
    events = Event.objects.all().order_by('event_date')
    return render(request, 'events/events.html', {'events': events})

def event_error_checker(request,event_form):
    """A view that checks for errors in event forms. Will be called when needed to abide by DRY"""
    if event_form.cleaned_data['event_date'] < datetime.datetime.now().date():
        messages.error(request, 'The event date cannot be in the past.')
    elif event_form.cleaned_data['event_date'] == datetime.datetime.now().date():
        messages.error(request, 'The event date cannot be today. The event must be posted atleast a day before the event date.')
    else:
        event_form = event_form.save(commit=False)
        event_form.event_location = event_form.event_location.title()
        event_form = event_form.save()

def add_event(request):
    """The view that facilitates the adding of events"""
    print(request.user.is_worshipper)
    if request.user.is_staff:
        if request.method == 'POST':
            event_form = EventForm(request.POST)
            if event_form.is_valid():
                event_error_checker(request, event_form)
                if event_form.cleaned_data['event_date'] > datetime.datetime.now().date():
                    return redirect('events:event')
            else:
                event_form = EventForm()
                messages.error(request, 'The event could not be added.')
        else:
            event_form = EventForm()
    else:
        return HttpResponse('You are not authorized to view this page.')
    return render(request, 'events/event_form.html', {'event_form': event_form})

def event_detail(request, event_id):
    """The view that facilitates the display of event details"""
    event = Event.objects.get(event_id=event_id)
    questions = Question.objects.filter(event=event)
    answers = Answer.objects.filter(event=event)
    return render(request, 'events/event_details.html', {'event': event, 'questions': questions, 'answers': answers})

def update_event(request, event_id):
    """The view to modify/update previously posted events."""
    event = Event.objects.get(event_id=event_id)
    if request.user.is_staff:
        if request.method == 'POST':
            update_event_form = UpdateEventForm(request.POST, instance=event)
            if update_event_form.is_valid():
                event_error_checker(request, update_event_form)
                if update_event_form.cleaned_data['event_date'] > datetime.datetime.now().date():
                    return redirect('events:event')
            else:
                update_event_form = UpdateEventForm()
                messages.error(request, 'The event could not be updated.')
        else:
            update_event_form = UpdateEventForm()
    else:
        return HttpResponse('You are not authorized to view this page.')
    return render(request, 'events/update_event.html', {'update_event_form': update_event_form, 'event': event,})

def del_event(request, event_id):
    """The view that facilitates the deletion of events"""
    if request.user.is_staff:
        event = Event.objects.get(event_id=event_id)
        event.delete()
        return redirect('events:event')
    return render(request, 'events/event_details.html')

def ask_question_temp(request, event_id):
    event = Event.objects.get(event_id=event_id)
    return render(request, 'events/ask_question.html', {'event': event})

def ask_question(request, event_id):
    """The view that facilitates asking questions about events"""
    context = {}
    if request.user.is_authenticated:
        if request.method == 'POST':
            question_form = QuestionForm(request.POST)
            if question_form.is_valid():
                event = Event.objects.get(event_id=event_id)
                question_form = question_form.save(commit=False)
                question_form.event = event
                question_form.user = UserProfile.objects.get(username=request.user.username)
                question_form.save()
                context['event'] = event
                return redirect('events:event_detail', event_id)
            else:
                question_form = QuestionForm()
        question_form = QuestionForm()
    else:
        return HttpResponse('You are not authorized to ask question. You need to be logged in.')
    context['question_form'] = question_form
    return render(request, 'events/ask_question.html', context)

def ans_question(request, qtn_id):
    """The view that facilitates asking questions about events"""
    context = {}
    if request.user.is_staff:
        if request.method == 'POST':
            ans_form = AnswerForm(request.POST)
            if ans_form.is_valid():
                qtn = Question.objects.get(question_id=qtn_id)
                ans_form = ans_form.save(commit=False)
                ans_form.question = qtn
                ans_form.event = ans_form.question.event
                ans_form.user = UserProfile.objects.get(username=request.user.username)
                ans_form.save()
                context['qtn'] = qtn
                return redirect('events:event_detail', qtn_id)
            else:
                ans_form = AnswerForm()
        ans_form = AnswerForm()
    else:
        return HttpResponse('You are not authorized to ask question. You need to be logged in.')
    context['ans_form'] = ans_form
    return render(request, 'events/ans_question.html', context)

def ans_question_temp(request, qtn_id):
    qtn = Question.objects.get(question_id=qtn_id)
    return render(request, 'events/ans_question.html', {'qtn': qtn})