
from django.db import models
from django.contrib.auth.models import User
from category.models import Category

# Create your models here.
# 	DEFAULT_COUNTRY_ID = id # id of Israel
class Blog(models.Model):
	category = models.ForeignKey(Category)
	blog_name = models.CharField(max_length=100)
	developer_name = models.CharField(max_length=100)

	def __unicode__(self):
		return self.blog_name