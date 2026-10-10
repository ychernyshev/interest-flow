from django.shortcuts import render
from django.contrib.auth import logout

from .forms import BaseUserCreationForm


# Create your views here.
def home(request):
    return render(request, 'inflow/home.html')


def login(request):
    return render(request, 'inflow/login.html')

def register(request):
    form = BaseUserCreationForm()
    return render(request, 'inflow/register.html')

def logout(request):
    logout(request)
