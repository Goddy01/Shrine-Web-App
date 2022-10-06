from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        exclude = ('event_id', )

class UpdateEventForm(forms.ModelForm):
    class Meta:
        model = Event
        exclude = ('event_id', )