from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


# Create your views here.
def login(request)
	form = AuthenticationForm()
	return render(request, 'fcd/login.html', {'form':form})