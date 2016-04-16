from django import template

register = template.Library()
from userprofile.models import UserProfile
from django.contrib.auth.models import User

def get_profile(value):
	try:
		profile = User.objects.get(username = value)
		data = UserProfile.objects.filter(user__username = profile)
	except:
		data = []
	return data

register.filter('get_profile', get_profile)