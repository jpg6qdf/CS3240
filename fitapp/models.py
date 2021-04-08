from django.db import models
from django.contrib.auth.models import User
import datetime
from django import forms
from django.utils import timezone


# Create your models here.
class User(models.Model):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    current = models.IntegerField(default=0) # bar part of progress bar
    maximum = models.IntegerField(default=100) # maximum length bar can be
    level = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.user.username} Profile'

    def update_level(self):
        if current >= maximum:
            current = current - 100
            level += 1

# logs model
class Logs(models.Model):
    exercise = models.CharField(max_length=200)#, help_text="title.")
    date = models.CharField(max_length=200)#, help_text="text.")      #could be slider, buttons, etc
    duration = models.CharField(max_length=200)#, help_text="text.")      #could be slider, buttons, etc.        ##also includes reps.
    intensity = models.CharField(max_length=200)#, help_text="text.")     #could be slider, buttons, etc
    area = models.CharField(max_length=200)#, help_text="text.")     #could be slider, buttons, etc
    ## can include other relevant info we want to encourage
    def __str__(self):
        return self.date + ":" + self.exercise + "\n"