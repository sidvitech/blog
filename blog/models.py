from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date

class UserProfile(models.Model):
	user=models.OneToOneField(User)
	first_name=models.CharField(max_length=50)
	last_name=models.CharField(max_length=50)
	email=models.EmailField()
	def __unicode__(self):
		return self.user.username

class Posts(models.Model):
	title=models.CharField(max_length=100)
	details=models.TextField()
	comments=models.CharField(max_length=150)
	likes=models.IntegerField(default=0)
	views=models.IntegerField(default=0)
	stars=models.IntegerField(default=0)
	def __unicode__(self):
		return self.title

