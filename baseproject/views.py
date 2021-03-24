from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.views.generic import CreateView

from .models import User

class UserProfile(CreateView):
    model = User
    fields = ('name', 'achievements')
    context_object_name = 'achievements'