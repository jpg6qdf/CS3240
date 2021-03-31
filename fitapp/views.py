from django.shortcuts import render
from .models import User 
from django.views import generic
from django.views.generic.base import TemplateView

# Create your views here.

class ProgressBar(TemplateView):
    model = User
    template_name = 'fitapp/progress.html'
    # def get(self, request):
    #     object1 = User.objects.all()
    #     return 

