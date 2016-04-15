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

def comment_count(value):
	count = 0
	if value:
		post_obj = PostAdd.objects.get(postname=value)
		count = CommentAdd.objects.filter(postname=post_obj).count()
	return count
register.filter('comment_count',comment_count)		