from django.db import models
from category.models import Category
# Create your models here.
class Blogapp(models.Model):
	category= models.ForeignKey(Category)
	blogname=models.CharField(max_length=200)
	visibility = models.CharField(max_length = 200)

	def __unicode__(self):
		return self.blogname
