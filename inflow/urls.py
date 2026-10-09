from django.urls import path

from inflow.views import home, login, register, logout

urlpatterns = [
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout, name='logout'),
    path('', home, name='home'),
]