from django.db import models
from django.contrib.auth.models import User
from userblog.models import Blog

# Create your models here.

class Post(models.Model):
	blog_name = models.ForeignKey(Blog)
	image = models.FileField(upload_to="images/",blank=True,null=True)
	title = models.CharField(max_length=100)
   	date_created = models.DateField()
	tag = models.CharField(max_length=200)
	body = models.TextField()

	def get_absolute_url(self):
		return "/blog/%d%02d%s/" % (self.date_created.month)
		
	def __unicode__(self):
		return self.title


class MyComment(models.Model):
	post_name = models.ForeignKey(Post, on_delete=models.CASCADE)
	title = models.CharField(max_length=250)

	def __unicode__(self):
		return self.title

class Like(models.Model):
	user = models.OneToOneField(User)
	like = models.BooleanField(default=False)

	def __unicode__(self):
		return self.user.username

