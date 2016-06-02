from django.conf.urls import patterns, url, include
from blog import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
	url(r'^$', views.blog,name='blog'),
	url(r'^my_posts/$', views.my_posts,name='my_posts'),
	url(r'^my_posts/(?P<page_no>[\w\-]+)/$', views.my_posts_list,name='my_posts'),
	url(r'^register/', views.register, name='register'),
    url(r'^logout/', views.user_logout, name='logout'),
	url(r'^my_profile/', views.my_profile, name='my_profile'),
	url(r'^edit_profile/', views.edit_profile, name='edit_profile'),
	url(r'^view_post/(?P<post_id>[\w\-]+)/', views.view_post, name='view_post'),
	url(r'^add_post/', views.add_post, name='add_post'),
	url(r'^search/', views.search, name='search'),
	url(r'^category_list/$', views.category_list, name='category_list'),
	url(r'^add_category/$', views.add_category, name='add_category'),
	url(r'^category/(?P<category_name>[\w\-]+)/$', views.category, name='category'),
	url(r'^user_profile/(?P<u_id>[\w\-]+)/$', views.user_profile, name='user_profile'),
	url(r'^post_search/', views.post_search, name='post_search'),
	url(r'^delete_comment/(?P<comment_id>[\w\-]+)-(?P<post_id>[\w\-]+)/$', views.delete_comment, name='delete_comment'),
	url(r'^delete_post/(?P<post_id>[\w\-]+)/', views.delete_post, name='delete_post'),


	url(r'^posts/(?P<page_no>[\w\-]+)/', views.posts_list, name='posts_list'),
	
] 

