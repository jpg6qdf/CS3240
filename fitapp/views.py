from .models import User 
from django.views import generic
from django.views.generic.base import TemplateView
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from django.urls import reverse
from django.utils import timezone
from .models import Logs, User
from .forms import LogsForm

# Create your views here.

class ProgressBar(TemplateView):
    model = User
    template_name = 'fitapp/progress.html'
    # def get(self, request):
    #     object1 = User.objects.all()
    #     return 



def Logs(request): ##doesn't need index. does have list though. Can be a generic detailview.
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = LogsForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            #form.save()

            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = LogsForm()
    return render(request, 'fitapp/Logs.html', {'form': form})

def setCurrent(request):

    user.user.current.update_level()

def Achievements(request):
    if request.method == 'POST':
        return HttpResponseRedirect('/')
    else:
        num = user.user.level + 10
    return render(request, 'fitapp/achievements.html', {'num': num})
