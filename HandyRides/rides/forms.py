from django import forms
from .models import Person
from django.forms import DateInput, TimeInput, TextInput


class RideForm(forms.Form):
  origination_city = forms.CharField(label='Origination City', max_length=64, required=False)
  origination_state = forms.CharField(label='Origination State', max_length=2, required=False)
  destination_city = forms.CharField(label='Destination City', max_length=64, required=False)
  destination_state = forms.CharField(label='Destination State', max_length=2, required=False)
  date = forms.DateField(required = False, widget=forms.DateInput(attrs={'placeholder': 'Select a date', 'type': 'date'}))
  time = forms.TimeField(required = False, widget=forms.TimeInput(attrs={'placeholder': 'Select a time', 'type': 'time'}))
  seats = forms.IntegerField(required = False)


class NewRideForm(forms.ModelForm):
  class Meta:
    model = Person

    widgets = {
            'date': DateInput(attrs={'placeholder': 'Select a date', 'type': 'date'}),
            'time': TimeInput(attrs={'placeholder': 'Select a time', 'type': 'time'}),
            'phone_number':TextInput(attrs={'placeholder': '999-999-9999'}),
            'email': TextInput(attrs= {'placeholder': 'example@example.com'}),
            'vehicle_type': TextInput(attrs= {'placeholder': 'Nissan'}),
            'vehicle_model': TextInput(attrs= {'placeholder': 'Sentra'}),
        }
    exclude = []

