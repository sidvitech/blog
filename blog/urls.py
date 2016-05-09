from django.conf.urls import patterns, url, include
from blog import views

urlpatterns=[
	url(r'^$', views.home, name='home'),
	url(r'^login/', views.user_login, name='login'),
	url(r'^register/', views.register, name='register'),
	url(r'^add_post/', views.add_post, name='add_post'),

]