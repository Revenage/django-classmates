from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import SignUpForm

# Create your views here.
def startpage(request):
    return render(request, 'app/startpage.html', {'body_class': 'text-center'})

def home(request):
    return render(request, 'app/home.html', {'body_class': 'text-center'})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

def log_in(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        auth.login(request, user)
        return redirect('home')
    else:
        return redirect('signup')

def log_out(request):
    logout(request)
    return redirect('home')

def error_404(request):
    return render(request,'error/404.html', {'data': {}})

def error_500(request):
    return render(request,'error/500.html', {'data': {}})