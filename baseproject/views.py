from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .models import Logs
from .forms import LogsForm

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
            return HttpResponseRedirect('Logs')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = LogsForm()
    return render(request, 'Logs.html', {'form': form})


#def listView(request):
#    thoughtslist = Thoughts.objects.all()
#    context = {
#        'loglist' : thoughtslist
#    }
#    template_name = 'thoughts/list'
#    return render(request, 'list.html', context)
##other has results, detail, and index view classes.
## as well as def vote.