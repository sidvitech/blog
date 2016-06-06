from django.conf.urls import url
from category.views import (
	create_category, 
	category_list,
	delete_category,
	category_detail,
	)


urlpatterns = [
    url(r'^create_category/', create_category, name="create_category"),
    url(r'^category_list/', category_list, name="category_list"),
    url(r'^delete_category/(?P<pk>[0-9]+)', delete_category, name="delete_category"),
	url(r'^delete_category/(?P<pk>[0-9]+)', delete_category, name="delete_category"),
    url(r'^(?P<pk>[0-9]+)/', category_detail, name="category_detail"),
    ]