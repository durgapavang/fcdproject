from django.urls import path
from . import views

urlpatterns = [
	path('', include('fcdtest.urls')),
    path('', views.login, name='login'),
]