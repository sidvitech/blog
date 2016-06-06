from django.db import models
from django.contrib.auth.models import User
from category.models import Category
import datetime

# Create your models here.

class Post(models.Model):
	user = models.ForeignKey(User)
	category = models.ForeignKey(Category)
	title = models.CharField(max_length=100)
	image = models.ImageField(upload_to="images/", blank=True)
   	created = models.DateTimeField(auto_now=False, auto_now_add=True)
	body = models.TextField()
	views = models.IntegerField(default=0)	

	def get_absolute_url(self):
		return "/blog/%d%02d%s/" % (self.date_created.month)
		
	def __unicode__(self):
		return self.title

class MyComment(models.Model):
	user = models.ForeignKey(User)
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	comment = models.BooleanField(default=False)

	def __unicode__(self):
		return self.title

class Like(models.Model):
	user = models.ForeignKey(User)
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	like = models.BooleanField(default=False)
	view=models.IntegerField(default=0)
	
	def __unicode__(self):
		return self.user.username

class Reply(models.Model):
	user = models.ForeignKey(User)
	post = models.ForeignKey(Post)
	comment = models.ForeignKey(MyComment)
	title = models.CharField(max_length=200)

	def __unicode__(self):
		return self.title
		
class PostView(models.Model):
    post = models.ForeignKey(Post, related_name='postviews')
    ip = models.CharField(max_length=40)
    session = models.CharField(max_length=40)
    created = models.DateTimeField(default=datetime.datetime.now())