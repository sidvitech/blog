from django.conf.urls import include, url
from django.contrib import admin
from post import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	url(r'^$',views.post_view, name='posthome'),
	url(r'^postcreate/$',views.post_create,name = 'postcreate'),
	url(r'^commentcreate/$',views.comment_create, name= 'commentcreate'),
	]