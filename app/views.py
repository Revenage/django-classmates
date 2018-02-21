from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseForbidden

# Create your views here.
def startpage(request):
    return render(request, 'app/startpage.html', {'body_class': 'text-center'})

def home(request):
    if request.user.is_authenticated:
        return render(request, 'app/home.html', {'body_class': 'text-center'})
    else:
        return HttpResponseForbidden()

def error_403(request):
    return render(request, 'error/403.html', {'data': {}})
    
def error_404(request):
    return render(request, 'error/404.html', {'data': {}})

def error_500(request):
    return render(request, 'error/500.html', {'data': {}})