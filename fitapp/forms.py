from django import forms
from .models import Logs

#import floppyforms as forms

#class Slider(forms.RangeInput):
#    min = 5
#    max = 20
#    step = 5
#    template_name = 'slider.html'

#    class Media:
#        js = (
 #           'js/jquery.min.js',
  #          'js/jquery-ui.min.js',
   #     )
   #     css = {
    #        'all': (
     #           'css/jquery-ui.css',
      #      )
      #  }

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

    #duration = forms.IntegerField(widget=Slider)

    ##def clean_duration(self):
        #duration = self.cleaned_data['duration']
        #if not 5 <= duration <= 20:
            #raise forms.ValidationError("Enter a value between 5 and 20")

        #if not duration % 5 == 0:
           # raise forms.ValidationError("Enter a multiple of 5")
        #return duration

    class Meta:
        model = Logs
        fields = ('exercise', 'date', 'intensity', 'duration')

        #duration = models.IntegerField(widget=forms.NumberInput(attrs={'type':'range', 'step': '5', 'min': '-100', 'max': '100', 'id':'myRange'}), required=False)
        widgets = {
            'date': DateInput(),
            'duration': forms.NumberInput(attrs={'max': '100', 'type':'range', 'step': '1', 'min': '0', 'id':'myRange'})
        }