from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class User(models.Model):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    #on_delete = models.DO_NOTHING
    value = models.IntegerField(default=20)
    maximum = models.IntegerField(default=100)

    