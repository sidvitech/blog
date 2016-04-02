from django.conf.urls import include, url
from django.contrib import admin
from blogapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	url(r'^$',views.blog_view, name='bloghome'),
	url(r'^createblog/$',views.blog_create, name ='createblog'),
	url(r'^deleteblog/$',views.bolg_delete, name='deleteblog'),
	]