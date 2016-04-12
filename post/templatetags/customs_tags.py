from django import template

register = template.Library()
from post.models import Post, MyComment

def get_post(value):
	print value
	try:
		print "try"
		post = Post.objects.get(title=value)
		data = MyComment.objects.filter(post_name=post)
	except:
		data = []
	return data

register.filter('get_post', get_post)

def get_image(value):
	print value
	try:
		print "try"
		post = Post.objects.get(image=value)
		data = MyComment.objects.filter(post_name=post)
	except:
		data = []
	return data

register.filter('post_name', get_image)