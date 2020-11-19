from django.urls import path
from . import views
from fcdtest import views

urlpatterns = [
    path('', views.login, name='login'),
    path('login', views.login, name='login'),
    path('dashboard', views.dashboard, name='dashboard'),
    # path('logout/')
]