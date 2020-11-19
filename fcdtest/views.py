from django.shortcuts import render
from django.http import HttpResponse
import mysql.connector
from operator import itemgetter 
from .models import User

# Create your views here.
def login(request):
	if request.method == 'POST':
		# user = User()
		# user.email = request.POST['email']
		# user.password = request.POST['password']
		print("dfds")
	else:
		return render(request, 'login.html')
	
def dashboard(request):
	return render(request, 'dashboard.html')