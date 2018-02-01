from __future__ import unicode_literals

from django.db import models

# Create your models here.

class UserManager(models.Manager):
    def validate(self, postData):
        errors = {}
        response = {
            'status' : True,
        }
        if len(postData['first_name']) < 3:
            errors['first_name'] = "please enter a longer name"
        if len(postData['email']) < 1:
            errors['email'] = "email needs to be supplied"
        else:
            existing = User.objects.filter(email = postData['email'].lower())
            if len(existing) > 0:
                print 'the email validation is working'
                errors['email'] = 'that email is already taken'
                    
        if len(errors) > 0:
            response['errors'] = errors
            response['status'] = False
        else:
            response['user'] = User.objects.create(
                first_name = postData['first_name'], 
                last_name = postData['last_name'], 
                email = postData['email'], 
                password = postData['password'])

        return response

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()