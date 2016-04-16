from django.conf.urls import include, url
from django.contrib import admin
from userprofile import views

urlpatterns = [
	url(r'^$',views.viewuserprofile, name='home'),
	url(r'^create/$', views.adduserprof_view, name='create_userprofile'),
	url(r'^update/$', views.updateuserprof_view, name='update_userprofile'),
	url(r'^editprofile/$',views.edit_profile, name='editprofile'),
	url(r'^updatepic/$',views.update_pic, name='updatepic'),
	]
