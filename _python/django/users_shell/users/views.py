from django.shortcuts import render, redirect
from . import models
from .models import Users
def index(request):

	context  = {
		'users_all' : Users.objects.all()
	}
	return render(request, 'index.html', context)

def add_user(request):
	new_user_first_name= request.POST['first_name']
	new_user_last_name = request.POST['last_name']
	new_user_email_address = request.POST['email_address']
	new_user_age = request.POST['age']
	Users.objects.create(first_name = new_user_first_name, last_name = new_user_last_name,
						email_address = new_user_email_address, age = new_user_age)
	return redirect('/')
