from django.urls import path
from . import views


app_name = 'fitapp'
urlpatterns = [
    path('progress/', views.ProgressBar.as_view(), name='progress'),
    path('achievements/', views.Achievements, name='achievements'),
    path('Logs/', views.LogReq, name='Logs'),
    path('viewLogs/', views.viewLogs, name='viewLogs'),
]