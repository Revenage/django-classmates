from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseForbidden, HttpResponse
import json

# Create your views here.
def startpage(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        return render(request, 'app/startpage.html', {'body_class': 'text-center'})

def error_403(request):
    return render(request, 'error/403.html', {'data': {}})
    
def error_404(request):
    return render(request, 'error/404.html', {'data': {}})

def error_500(request):
    return render(request, 'error/500.html', {'data': {}})