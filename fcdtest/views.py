from django.shortcuts import render
from django.http import HttpResponse
import mysql.connector
from operator import itemgetter 
from .models import User

# Create your views here.
def login(request):
	if request.method == 'POST':
		user = User()
		user.email = request.POST['email']
		user.password = request.POST['password']
		print(user)
		return render(request, 'dashboard.html')
	else:
		return render(request, 'login.html')
	
def dashboard(request):
	if request.method == 'POST':
		return render(request, 'dashboard.html')
	else:
		return render(request, 'dashboard.html')
