from django.db import models
from blogapp.models import Blogapp
from django.contrib.auth.models import User
# Create your models here.
class PostAdd(models.Model):
	user = models.ForeignKey(User)
	blogname=models.ForeignKey(Blogapp)
	postname = models.CharField(max_length = 200,unique =True) 
	# choice = models.CharField(max_length =200)
	text = models.TextField()
	picture = models.FileField(null=True, blank=True)	
	visibility = models.CharField(max_length = 200)

	def __unicode__(self):
		return self.postname

class CommentAdd(models.Model):
	# serializer_class = CommentSerializer
	# user = models.ForeignKey(User)
	postname = models.ForeignKey(PostAdd,null=True,blank=True)
	comment = models.TextField(blank=True)

	def __unicode__(self):
		return self.comment