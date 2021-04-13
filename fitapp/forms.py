from django import forms
from .models import Logs

class DateInput(forms.DateInput):
    input_type = 'date'

class RangeInput(forms.NumberInput):
    input_type = 'range'

class LogsForm(forms.ModelForm):
#    exercise = forms.CharField(max_length=10, choices=EXERCISE_CHOICES, default='other')#, help_text="title.")
#    date = forms.CharField(max_length=200)#, help_text="text.")      #could be slider, buttons, etc
#    duration = forms.CharField(max_length=200)#, help_text="text.")      #could be slider, buttons, etc.        ##also includes reps.
#    intensity = forms.CharField(max_length=200)#, help_text="text.")     #could be slider, buttons, etc
    #area = forms.CharField(max_length=200)#, help_text="text.")     #could be slider, buttons, etc
    ## can include other relevant info we want to encourage
    class Meta:
        model = Logs
        fields = ('exercise', 'date', 'intensity', 'area', 'duration')
        widgets = {
            'date': DateInput(),
            'duration': forms.NumberInput(attrs={'max': '100', 'type':'range', 'step': '1', 'min': '0', 'id':'myRange'})
        }