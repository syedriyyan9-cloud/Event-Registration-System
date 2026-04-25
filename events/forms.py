from .models import Events
from django import forms

class EventForm(forms.ModelForm):
    '''form for event table'''
    class Meta:
        model = Events
        fields = ['event_name', 'event_venue', 'event_date', 'event_capacity', 'event_type', 'event_details']
        widgets = {
            'event_date': forms.DateTimeInput(attrs={'type':'datetime-local'}),
            'event_details': forms.Textarea(attrs={'rows':5,'placeholder':'Add details for event'}),
            'event_name':forms.TextInput(attrs={'placeholder':'Name of the Event'}),
            'event_venue':forms.TextInput(attrs={'placeholder':'Place for event'}),
            'event_capacity':forms.TextInput(attrs={'placeholder':'Number of People e.g 20'}),
            'event_type':forms.TextInput(attrs={'placeholder':'Type of event'}),
        }