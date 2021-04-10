from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    level = models.IntegerField(default=0)
    current = models.IntegerField(default=0) # bar part of progress bar
    maximum = models.IntegerField(default=100) # maximum length bar can be
    def __str__(self):
        return f'{self.user.username} Profile'

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

# logs model
class Logs(models.Model):
    exercise = models.CharField(max_length=200)#, help_text="title.")
    date = models.CharField(max_length=200)#, help_text="text.")      #could be slider, buttons, etc
    duration = models.CharField(max_length=200)#, help_text="text.")      #could be slider, buttons, etc.        ##also includes reps.
    intensity = models.CharField(max_length=200)#, help_text="text.")     #could be slider, buttons, etc
    area = models.CharField(max_length=200)#, help_text="text.")     #could be slider, buttons, etc
    ## can include other relevant info we want to encourage
    # owner = models.ForeignKey(siteUser, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.date + ":" + self.exercise + "\n"