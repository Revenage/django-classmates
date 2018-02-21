from django.shortcuts import render
from .forms import SignUpForm

def signup(request):
    return render(request, 'registration/signup.html', {'body_class': 'text-center'})
# Create your views here.
