from django.conf.urls import include, url
from django.contrib import admin
from post import views

app_name='post'
urlpatterns = [
	url(r'^$',views.post_view, name='posthome'),
	url(r'^create/$',views.post_create,name = 'postcreate'),
	url(r'^comment/create/$',views.comment_create, name= 'commentcreate'),
	url(r'^comment/view/$',views.comment_view, name = 'commentview'),
	url(r'^comment/edit/$',views.comment_edit, name='commentedit'),
	url(r'^postlist/$',views.post_list, name='postlist'),
	url(r'^(?P<pk>[0-9]+)/$',views.post_detail, name='post_detail'),
	]
