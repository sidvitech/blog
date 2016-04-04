
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserRegistration(models.Model):
	user = models.OneToOneField(User)
	birthday = models.DateField()
	name = models.CharField(max_length=100)

	def __unicode__(self):
		return self.name

