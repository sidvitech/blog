from django import template

register = template.Library()
from post.models import Post, MyComment, Like
from category.models import Category

def get_post(value):
	try:
		post = Post.objects.get(title=value)
		data = MyComment.objects.filter(post=post)
	except:
		data = []
		print data
	return data

register.filter('get_post', get_post)

def check_like(value, user):
	is_like = False;
	try:
		post = Post.objects.get(title=value)
		like = Like.objects.get(user=user, post=post)
		is_like = like.like
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

def comment_count(value):
	count = 0
	if value:
		post_obj = Post.objects.get(title=value)
		count = MyComment.objects.get(post=post_obj, comment=True).count()
		
	return count

register.filter('comment_count', comment_count)

def post_count(value):
	count = 0
	if value:
		post_obj = Category.objects.get(title=value)
		count = Post.objects.get(category=post_obj).count()
		print count 
		print "Count post in category"
		
	return count

register.filter('post_count', post_count)