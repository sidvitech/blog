
from django.db import models
from django.contrib.auth.models import User
from userauth.models import UserRegistration


# Create your models here.
# 	DEFAULT_COUNTRY_ID = id # id of Israel
class Category(models.Model):
	user_register_name = models.ForeignKey(UserRegistration)
	name = models.CharField(max_length=100)
	user_name = models.CharField(max_length=100)

	def __unicode__(self):
		return self.name