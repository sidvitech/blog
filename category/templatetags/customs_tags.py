from django import template

register = template.Library()
from category.models import Category

def category_count(value):
	count = 0
	if value:
		post_obj = Category.objects.get(name=value)
		count = MyComment.objects.get(post=post_obj, comment=True).count()
		
	return count

register.filter('category_count', category_count)