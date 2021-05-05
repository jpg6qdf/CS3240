"""
*  REFERENCES
*
*  Title: Creating Comments System With Django
*  Author: Django Central
*  URL: https://djangocentral.com/creating-comments-system-with-django/
"""
from django.views.generic.base import TemplateView
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from django.urls import reverse
from django.utils import timezone
from .models import Logs, Profile, User, Comment
from .forms import LogsForm, CommentForm
from django.contrib.auth.backends import BaseBackend
from django.db.models import F

from django.contrib.auth.decorators import login_required

@login_required(login_url='/')
def ProgressBar(request):
    return render(request, 'fitapp/progress.html')
    # def get(self, request):
    #     object1 = User.objects.all()
    #     return 


@login_required(login_url='/')
def LogReq(request): ##doesn't need index. does have list though. Can be a generic detailview.
    try:
        user = request.user
        form = LogsForm()
    except User.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'fitapp/Logs.html', {'user': user, 'form': form})

@login_required(login_url='/')
def updatelogs(request, user_id):
    user = User.objects.get(pk=user_id)
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = LogsForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            #form.save()
            log = Logs(exercise=form.cleaned_data['exercise'],
                date=form.cleaned_data['date'], 
                duration=form.cleaned_data['duration'],
                intensity=form.cleaned_data['intensity'],
                area=form.cleaned_data['area'],
                owner=request.user.profile
            )
            log.save()
            user = User.objects.get(pk=user_id)
            user.profile.current = user.profile.current + log.duration
            if log.intensity == 'light':
                user.profile.current = user.profile.current + 5
            elif log.intensity == 'moderate':
                user.profile.current = user.profile.current + 10
            elif log.intensity == 'vigorous':
                user.profile.current = user.profile.current + 15
            while user.profile.current >= 100:
                print(user.profile.current)
                user.profile.current = user.profile.current - 100
                user.profile.level = user.profile.level + 1
            user.save()
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect(reverse('fitapp:viewLogs'))
    # if a GET (or any other method) we'll create a blank form
    else:
        form = LogsForm()
    return render(request, 'fitapp/Logs.html', {'form': form, 'user': user})

@login_required(login_url='/')
def viewLogs(request):
    template = loader.get_template('fitapp/viewLogs.html')
    if request.method != 'GET':
        raise Exception('Should be a GET request')
    logs = Logs.objects.order_by("-date") 
    my_logs = Logs.objects.filter(owner=request.user.profile).all()
    context = {'logs' : logs, 'my_logs' : my_logs}
    return HttpResponse(template.render(context, request))

def userLogs(request, user_id):
    print(user_id)
    user = User.objects.get(pk=user_id)
    user_logs = Logs.objects.filter(owner=user.profile)
    return render(request, 'fitapp/userLogs.html', {'logs': user_logs, 'user': user})

@login_required(login_url='/')
def update(request, user_id):
    user = User.objects.get(pk=user_id)
    user.profile.current = user.profile.current + 10
    while user.profile.current >= 100:
        print(user.profile.current)
        user.profile.current = user.profile.current - 100
        user.profile.level = user.profile.level + 1
    user.save()
    return render(request, 'fitapp/progress.html')

@login_required(login_url='/')
def log(request, logs_id):
    user = request.user
    template = loader.get_template('fitapp/log.html')
    log_accessed = get_object_or_404(Logs, pk=logs_id)
    log_comments = Comment.objects.filter(post=log_accessed)
    context = {'log' : log_accessed, 'comments': log_comments, 'user' : user}
    return HttpResponse(template.render(context, request))

# begin Creating Comments code #
@login_required(login_url='/')
def post_detail(request, logs_id):
    user = request.user
    template_name = loader.get_template('fitapp/log.html')
    post = get_object_or_404(Logs, pk=logs_id)
    comments = post.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()
    context = {'log' : post, 'comments': comments, 'user' : user}

    return HttpResponse(template_name.render(context, request))
# end Creating Comments code #

@login_required(login_url='/')
def Achievements(request):
    try:
        user = request.user
        num = int((user.profile.level / 10)) + 10
    except User.DoesNotExist:
        raise Http404("User does not exist")
    return render(request, 'fitapp/achievements.html', {'user': user, 'num': num})

@login_required(login_url='/')
def deleteLog(request, logs_id):
    user = request.user.profile
    log = get_object_or_404(Logs, pk=logs_id)
    if log.owner != user:
        return HttpResponseRedirect('/')
    allComments = Comment.objects.all().filter(post=log)
    for comment in allComments:
        comment.delete()
    Logs.objects.filter(pk=logs_id).delete()
    return HttpResponseRedirect(reverse('fitapp:viewLogs'))

@login_required(login_url='/')
def leaderboard(request):
    try: 
        curruser = request.user
        currusername = request.user.username
        print(currusername)
        users = Profile.objects.all().order_by('-level','-current')
    except Profile.DoesNotExist:
        raise Http404("Profile does not exist")
    return render(request, 'fitapp/leaderboard.html', {'users': users, 'currusername': currusername})

def shareable(request, logs_id):
    template = loader.get_template('fitapp/shareable.html')
    log_accessed = get_object_or_404(Logs, pk=logs_id)
    log_comments = Comment.objects.filter(post=log_accessed)
    context = {'log' : log_accessed, 'comments': log_comments}    
    return HttpResponse(template.render(context, request))

