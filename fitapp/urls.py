from django.urls import path
from . import views


app_name = 'fitapp'
urlpatterns = [
    path('progress/', views.ProgressBar.as_view(), name='progress'),
    path('Logs/', views.Logs, name='Logs'),
]