from django.conf.urls import include, url
from django.contrib import admin
from userprofile import views

urlpatterns = [
	url(r'^$',views.viewuserprofile, name='home'),
	url(r'^create/$', views.adduserprofile, name='create_userprofile'),
	url(r'^update/$', views.updateuserprofile, name='update_userprofile'),
	url(r'^edit/$',views.edit_profile, name='edit_userprofile'),
	url(r'^picture/update/$',views.update_pic, name='update_pic'),
	]
