from django.db import models
from django.contrib.auth.models import User
import datetime
from django import forms
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class User(models.Model):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    current = models.IntegerField(default=0) # bar part of progress bar
    maximum = models.IntegerField(default=100) # maximum length bar can be
    def __str__(self):
        return f'{self.user.username} Profile'

EXERCISE_CHOICES = (
    ('pushup','pushup'),
    ('situp', 'situp'),
    ('pullup','pullup'),
    ('squat','squat'),
    ('burpee','burpee'),
    ('lift','lift'),
    ('run','run'),
    ('stretches','stretches'),
    ('other','other'),
)

INTENSITY_CHOICES = (
    ('light','light'),
    ('moderate', 'moderate'),
    ('vigorous','vigorous'),
)

DEFAULT_duration = 1
MAX_duration = 100
MIN_duration = 0

#DURATION should be slider
#DATE should be found using datepicker


# logs model
class Logs(models.Model):
    exercise = models.CharField(max_length=10, choices=EXERCISE_CHOICES, default='other')#, help_text="title.")
    date = models.DateField()#, help_text="text.")      #could be slider, buttons, etc
    #duration = models.CharField(max_length=200)#, help_text="text.")      #could be slider, buttons, etc.        ##also includes reps.
    
    duration = models.PositiveSmallIntegerField( name=('duration'), default=DEFAULT_duration,validators=[MinValueValidator(MIN_duration), MaxValueValidator(MAX_duration)])
        #_('duration'), 
    intensity = models.CharField(max_length=10, choices=INTENSITY_CHOICES, default='light')#, help_text="text.")     #could be slider, buttons, etc
    #area = models.CharField(max_length=200)#, help_text="text.")     #could be slider, buttons, etc
    ## can include other relevant info we want to encourage
    def __str__(self):
        return self.date + ":" + self.exercise + "\n"