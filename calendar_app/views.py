from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from django.http import HttpResponseForbidden, HttpResponse
import json

# Create your views here.
def calendar(request):
    return render(request, 'calendar_app/index.html', {'location': 'calendar'})
    
def json_test(request):
    response_data = {'test': 2, 'qwerty': 'test'}
    return HttpResponse(json.dumps(response_data), content_type="application/json")