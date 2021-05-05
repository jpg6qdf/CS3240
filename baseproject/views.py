"""
*  REFERENCES
*
*  Title: Logout
*  Author: Django Central
*  URL: https://docs.djangoproject.com/en/3.2/topics/auth/default/
"""


from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
    logout(request)
    return redirect('/')
