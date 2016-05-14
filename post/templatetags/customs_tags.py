from django import template

register = template.Library()
from post.models import Post, MyComment, Like

def get_post(value):
	try:
		post = Post.objects.get(title=value)
		data = MyComment.objects.filter(post_name=post)
	except:
		data = []
		print data
	return data

register.filter('get_post', get_post)

def check_like(value, user):
	is_like = False;
	print value, user
	try:
		post = Post.objects.get(title=value)
		like = Like.objects.get(user=user, post=post)
		is_like = like.like
		print is_like
	except:
		pass
 	return is_like

register.filter('check_like', check_like)


def like_count(value):
	count = 0
	if value:
		post_obj = Post.objects.get(title=value)
		count = Like.objects.filter(post=post_obj, like=True).count()
		
	return count

register.filter('like_count', like_count)


