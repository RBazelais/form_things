from __future__ import unicode_literals

from django.db import models

import re
import bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserValidator(models.Manager):
	def AddUser(self, name, email, password, confirm):
		errors = []
		if len(name) < 1:
			errors.append("name cannot be blank!")
		else:	
			for char in name:
				if str(char).isdigit():
				 	errors.append("No numbers in the name fields!") 
		if len(password) < 8:
			errors.append("Password must be at least 8 characters long!")
		else:
			hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())			
		if not EMAIL_REGEX.match(email):
			errors.append("Please enter a valid email address!")
		else:	
			emails = User.objects.filter(email=email)
			if len(emails) != 0:	
				errors.append("Email already taken!")
		if password != confirm:
			errors.append("Passwords must match!")
		if len(errors) > 0:
			return errors	
		else:
			new_user = User.objects.create(name=name, email=email, password=hashed)
			return new_user	
	def login(self, email, password):
		users = User.objects.filter(email=email)
		print users
		if len(users) == 0:
			return "Invalid email!"
		elif bcrypt.checkpw(password.encode(), users[0].password.encode()) == False:
			return "Incorrect password!"
		else:	
			return users[0]	

class User(models.Model):
	name = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	password = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	objects = UserValidator()
	
