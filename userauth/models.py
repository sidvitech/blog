from django.db import models

# Create your models here.
class registration(models.Model):
	uname=models.CharField(max_length=200)
	email=models.CharField(max_length=200)
	pwd=models.CharField(max_length=200)
	cfmpwd=models.CharField(max_length=200)

	def __unicode__(self):
		return self.uname