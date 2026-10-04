from django.urls import path

from inflow.views import home

urlpatterns = [
    path('', home, name='home'),
]