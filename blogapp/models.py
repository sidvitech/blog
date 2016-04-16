from django.db import models
from category.models import Category
from django.contrib.auth.models import User
# Create your models here.
class Blogapp(models.Model):
	user = models.ForeignKey(User)
	category= models.ForeignKey(Category)
	blogname=models.CharField(max_length=200)
	visibility = models.CharField(max_length = 200)

	def __unicode__(self):
		return self.blogname
