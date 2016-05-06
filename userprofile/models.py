
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserDetaile(models.Model):
	name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	mobile_no = models.CharField(max_length=10)
	gender = models.CharField(max_length=100)
	email_id = models.CharField(max_length=100)
	address = models.CharField(max_length=100)

	def __unicode__(self):
		return self.name