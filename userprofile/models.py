from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	designation = models.CharField(max_length=50, blank=True)
	birthdate = models.DateField(blank=True)
	lives_in = models.CharField(max_length=100, blank=True)
	profile_picture = models.ImageField(upload_to="images/user/profile_pictures/", blank=True)
	
	def __unicode__(self):
		return self.user.username