from django.db import models
from django.db.models import signals
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class UserProfile(models.Model):
	user = models.OneToOneField(User,null=True)
	gender = models.CharField(max_length=200,default='female',null=True,blank=True)
	mobileno=PhoneNumberField(default=0,blank=True,null=True)
	picture = models.ImageField(upload_to='profile_images', blank=True,null=True)	

	def __unicode__(self):
		return self.user.username

		
# def create_user(sender, instance, **kwargs):
#  	profile, new = UserProfile.objects.get_or_create(user=instance)
#  	print "save is called"	

# signals.post_save.connect(create_user, User)
