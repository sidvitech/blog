from django.conf.urls import patterns, url, include
from blog import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
	url(r'^$', views.home, name='home'),
	url(r'^register/', views.register, name='register'),
    url(r'^logout/', views.user_logout, name='logout'),
	url(r'^view_profile/', views.view_profile, name='view_profile'),
	url(r'^edit_profile/', views.edit_profile, name='edit_profile'),
	url(r'^view_post/(?P<post_id>[\w\-]+)/', views.view_post, name='view_post'),
	url(r'^add_post/', views.add_post, name='add_post'),
	url(r'^search/', views.search, name='search'),
	url(r'^category_list/$', views.category_list, name='category_list'),
	url(r'^category/(?P<category_name>[\w\-]+)/$', views.category, name='category'),

] 

