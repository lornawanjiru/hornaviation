from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import User
# Create your models here.


class Contact(models.Model):
       fname = models.CharField(max_length=100)
       lname = models.CharField(max_length=100)
       email = models.EmailField(max_length=254)
       subject = models.TextField()
       message = models.TextField() 
       Written = models.DateTimeField(auto_now_add=True) 

class Auth_user(models.Model):
       pic = models.ImageField(upload_to='img')
       superuser = models.BooleanField(default=False)
       username = models.CharField(max_length=100)
       date_joined = models.DateTimeField(auto_now_add=True)  