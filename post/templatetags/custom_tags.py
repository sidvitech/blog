from django import template

register = template.Library()
from post.models import CommentAdd, PostAdd

def get_post(value):
	try:
		post = PostAdd.objects.get(postname=value)
		data = CommentAdd.objects.filter(postname=post)
	except:
		data = []
	return data

register.filter('get_post', get_post)