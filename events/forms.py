from django import forms
from .models import Event, Question, Answer

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        exclude = ('event_id', )

class UpdateEventForm(forms.ModelForm):
    class Meta:
        model = Event
        exclude = ('event_id', )

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('question', )

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ('answer', )