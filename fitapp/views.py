from django.views.generic.base import TemplateView
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from django.urls import reverse
from django.utils import timezone
from .models import Logs, Profile, User
from .forms import LogsForm
from django.contrib.auth.backends import BaseBackend

# Create your views here.

class ProgressBar(TemplateView):
    model = Profile
    template_name = 'fitapp/progress.html'
    # def get(self, request):
    #     object1 = User.objects.all()
    #     return 



def LogReq(request): ##doesn't need index. does have list though. Can be a generic detailview.
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = LogsForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            #form.save()
            log = Logs(exercise=form.cleaned_data['exercise'],date=form.cleaned_data['date'], duration=form.cleaned_data['duration'],intensity=form.cleaned_data['intensity'],area=form.cleaned_data['area'])
            log.save()
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = LogsForm()
    return render(request, 'fitapp/Logs.html', {'form': form})

def viewLogs(request):
    template = loader.get_template('fitapp/viewLogs.html')

    if request.method != 'GET':
        raise Exception('Should be a GET request')
    
    logs = Logs.objects.all()
    context = {'logs' : logs}
    return HttpResponse(template.render(context, request))

def Achievements(request):
    if request.method == 'POST':
        return HttpResponseRedirect('/')
    else:
        user = request.user
        num = user.profile.level + 10

    return render(request, 'fitapp/achievements.html', {'num': num})

def update(request, user_id):
    user = User.objects.get(pk=user_id)
    user.profile.current = 10
    user.save()
    return render(request, 'fitapp/achievements.html')
