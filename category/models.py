from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
	user = models.ForeignKey(User)
	name = models.CharField(max_length=100)
	user_name = models.CharField(max_length=100)

	def __unicode__(self):
		return self.name
