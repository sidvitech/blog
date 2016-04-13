from django import template

register = template.Library()
from post.models import Post, MyComment

def get_post(value):
	try:
		post = Post.objects.get(title=value)
		data = MyComment.objects.filter(post_name=post)
	except:
		data = []
	return data

register.filter('get_post', get_post)