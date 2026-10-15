from django.shortcuts import render
from django.contrib.auth import logout

from .forms import BaseUserCreationForm, UserLoginForm


# Create your views here.
def home(request):
    return render(request, 'inflow/home.html')


def login(request):
    form = UserLoginForm()

    context = {
        'form': form,
        'title': 'Entering an account',
    }

    return render(request, 'inflow/login.html', context=context)

def register(request):
    form = BaseUserCreationForm()

    context = {
        'form': form,
        'title': 'Registration',
    }

    return render(request, 'inflow/register.html', context=context)

def logout(request):
    logout(request)
