from django import forms
from .models import Logs, Comment

from django.core.exceptions import ValidationError
from datetime import date

class DateInput(forms.DateInput):
    input_type = 'date'

class RangeInput(forms.NumberInput):
    input_type = 'range'

class LogsForm(forms.ModelForm):
    def clean_date(self):
            print(date.today())
            thisday = self.cleaned_data['date']
            if thisday > date.today():
                raise forms.ValidationError("The entered date is in the future.")                
            return thisday

    class Meta:
        model = Logs
        fields = ('exercise', 'date', 'intensity', 'area', 'duration')
        widgets = {
            'date': DateInput(),
            'duration': forms.NumberInput(attrs={'max': '500', 'type':'range', 'step': '1', 'min': '0', 'id':'myRange'})
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')
