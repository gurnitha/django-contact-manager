# apps/contact/models.py

# Django modules
from django.db import models
from django.utils.timezone import datetime
from django.contrib.auth.models import User

# Django locals

# Create your models here.

class Contact(models.Model):
	manager = models.ForeignKey(User,
		on_delete=models.RESTRICT, default=None)
	name  = models.CharField(max_length=50)
	email = models.CharField(max_length=100)
	phone = models.CharField(max_length=15)
	info  = models.CharField(max_length=50)
	gender = models.CharField(max_length=50, 
		choices=(
				('male', 'Male'), 
				('female', 'Female')))
	image = models.ImageField(upload_to='images/', blank=True)
	date_added = models.DateTimeField(default=datetime.now)

	class Meta: 
		ordering = ['-id']

	def __str__(self):
		return self.name

