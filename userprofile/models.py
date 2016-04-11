from django.db import models
# from PIL import Image
from django.db.models import signals
from django.contrib.auth.models import User

# Create your models here.



class userprof(models.Model):
	fname = models.CharField(max_length=200)
	lname = models.CharField(max_length=200)
	mobileno=models.IntegerField(default=0)
	gender=models.CharField(max_length=200)
	emailid=models.EmailField(unique=True)

	def __unicode__(self):
		return self.fname

class profilepic(models.Model):
	picture = models.ImageField(upload_to='profile_images', blank=True)		

class UserProfile(models.Model):
	user = models.OneToOneField(User,null=True)
	# user= models.ForeignKey(User, related_name='uploaded_by')
	gender = models.CharField(max_length=200,default='female',null=True,blank=True)
	mobileno=models.IntegerField(default=0,blank=True,null=True)
	picture = models.ImageField(upload_to='profile_images', blank=True,null=True)	

	def __unicode__(self):
		return self.user.username

		
# def create_user(sender, instance, **kwargs):
# 	profile, new = UserProfile.objects.get_or_create(user=instance)
# 	print "save is called"	

# signals.post_save.connect(create_user, User)
