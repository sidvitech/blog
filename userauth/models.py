
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserRegistration(models.Model):
	user = models.OneToOneField(User)
	image = models.FileField(upload_to="images/",blank=True,null=True)
	birthday = models.DateField()
	name = models.CharField(max_length=100)

	def __unicode__(self):
		return self.name

class View(models.Model):
	user = models.OneToOneField(User)
	view = models.BooleanField(default=False)

	def __unicode__(self):
		return self.user.username



