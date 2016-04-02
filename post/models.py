from django.db import models
from blogapp.models import Blogapp
# Create your models here.
class PostAdd(models.Model):
	blogname=models.ForeignKey(Blogapp)
	postname = models.CharField(max_length = 200) 
	choice = models.CharField(max_length =200)
	text = models.TextField()
	picture = models.ImageField(upload_to='profile_images', blank=True)	
	visibility = models.CharField(max_length = 200)

	def __unicode__(self):
		return self.postname

class CommentAdd(models.Model):
	postname = models.ForeignKey(PostAdd)
	comment = models.TextField()

	def __unicode__(self):
		return self.comment