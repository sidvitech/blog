from django.db import models
from blogapp.models import Blogapp
from django.contrib.auth.models import User
# Create your models here.
class PostAdd(models.Model):
	username = models.ForeignKey(User)
	blogname=models.ForeignKey(Blogapp)
	postname = models.CharField(max_length = 200) 
	# choice = models.CharField(max_length =200)
	text = models.TextField()
	picture = models.FileField(null=True, blank=True)	
	visibility = models.CharField(max_length = 200)

	def __unicode__(self):
		return self.postname

class CommentAdd(models.Model):
	postname = models.ForeignKey(PostAdd)
	comment = models.TextField()

	def __unicode__(self):
		return self.comment