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

def setCurrent(request):
    user.user.current.update_level()

def Achievements(request):
    if request.method == 'POST':
        return HttpResponseRedirect('/')
    else:
        field_object = User._meta.get_field("maximum")
        num = field_object.value_from_object(User.objects.get(id=request.user.id))

    return render(request, 'fitapp/achievements.html')

def viewLogs(request):
    template = loader.get_template('fitapp/viewLogs.html')

    if request.method != 'GET':
        raise Exception('Should be a GET request')
    
    logs = Logs.objects.all()
    context = {'logs' : logs}
    return HttpResponse(template.render(context, request))
