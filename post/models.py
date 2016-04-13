from django.db import models
from django.contrib.auth.models import User
from userblog.models import Blog

# Create your models here.

class Post(models.Model):
	blog_name = models.ForeignKey(Blog)
	title = models.CharField(max_length=100)
	image = models.ImageField(upload_to="images/",blank=True,null=True)
   	date_created = models.DateField()
	tag = models.CharField(max_length=200)
	body = models.TextField()
	like = models.BooleanField(default=False)

	def get_absolute_url(self):
		return "/blog/%d%02d%s/" % (self.date_created.month)
		
	def __unicode__(self):
		return self.title


class MyComment(models.Model):
	user = models.ForeignKey(User)
	post_name = models.ForeignKey(Post, on_delete=models.CASCADE)
	title = models.CharField(max_length=250)

	def __unicode__(self):
		return self.title

class Like(models.Model):
	user = models.OneToOneField(User)
	like = models.BooleanField(default=False)

	def __unicode__(self):
		return self.user.username


class Contact(models.Model):
	user_name = models.OneToOneField(User)
	contact_name = models.CharField(max_length=200)
	contact_email = models.CharField(max_length=200)
	content = models.TextField()

	def __unicode__(self):
		return self.contact_name