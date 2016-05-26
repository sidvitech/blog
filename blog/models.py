from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date

class UserProfile(models.Model):
	user=models.OneToOneField(User)
	designation=models.CharField(max_length=50, blank=True)
	birthdate=models.DateField(blank=True)
	lives_in=models.CharField(max_length=100, blank=True)
	profile_picture=models.ImageField(upload_to="user/profile_pictures/", blank=True)
	def __unicode__(self):
		return self.user.username

class Category(models.Model):
	user=models.ForeignKey(User)
	name = models.CharField(max_length=128, unique=True)
	total_posts = models.IntegerField(default=0)
	def __unicode__(self):
		return self.name


class Posts(models.Model):
	user=models.ForeignKey(User)
	title=models.CharField(max_length=100)
	details=models.TextField()
	thumb=models.ImageField(upload_to="blog/images/", blank=True)
	created_on=models.DateField(auto_now_add=True)
	category=models.ForeignKey(Category)
	likes=models.IntegerField(default=0)
	views=models.IntegerField(default=0)
	stars=models.IntegerField(default=0)
	
