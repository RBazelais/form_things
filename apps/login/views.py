from django.shortcuts import render, redirect
from models import User
from django.contrib import messages
import re
import datetime
import bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

def index(request):	
	return render(request, "index.html")

def process(request):
	if request.method == 'POST':
		new_user = User.objects.AddUser( #registering validation 
			request.POST['name'], 
			request.POST['email'],
			request.POST['password'],
			request.POST['confirm']
			)
		print new_user
		if type(new_user) is list:
			for error in new_user:
				messages.add_message(request, messages.ERROR, error)
			return redirect('/')
		else:
			request.session['user_id'] = new_user.id
			return redirect("/users/{}".format(new_user.id)) #new user returns to users page
	else:
		return redirect("/") 		

def login(request):	
	if request.method == 'POST':
		login = User.objects.login( #login validation 
			request.POST['email'],
			request.POST['password']
			)
		if type(login) is unicode:
			messages.add_message(request, messages.ERROR, login)
			return redirect('/')
		else:
			request.session['user_id'] = login.id
			return redirect("/users/{}".format(login.id))
		return redirect("/")
	else:
		return redirect("/")	

def logout(request):
	request.session.clear()	
	return redirect('/')

def user_dash(request, id):
	if 'user_id' not in request.session:
		return redirect('/')
	else:	
		user = User.objects.get(id=id)
		return render(request, "userview.html", {'user' : user})		
