import datetime
from django.db import models
from django import forms
from django.utils import timezone

class Logs(models.Model):
    exercise = models.CharField(max_length=200)#, help_text="title.")
    date = models.CharField(max_length=200)#, help_text="text.")      #could be slider, buttons, etc
    duration = models.CharField(max_length=200)#, help_text="text.")      #could be slider, buttons, etc.        ##also includes reps.
    intensity = models.CharField(max_length=200)#, help_text="text.")     #could be slider, buttons, etc
    area = models.CharField(max_length=200)#, help_text="text.")     #could be slider, buttons, etc
    ## can include other relevant info we want to encourage
    def __str__(self):
        return self.date + ":" + self.exercise + "\n"
