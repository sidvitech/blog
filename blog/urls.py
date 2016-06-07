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
	url(r'^like_post/', views.like_post, name="like_post"),
	url(r'^unlike_post/', views.unlike_post, name="unlike_post"),
	url(r'^star_post/', views.star_post, name="star_post"),
	url(r'^unstar_post/', views.unstar_post, name="unstar_post"),
	url(r'^post_comment/', views.post_comment, name="post_comment"),

	url(r'^add_post/', views.add_post, name='add_post'),
	url(r'^search/', views.search, name='search'),
	url(r'^category_list/$', views.category_list, name='category_list'),
	url(r'^add_category/$', views.add_category, name='add_category'),
	url(r'^category/(?P<category_name>[\w\-]+)/$', views.category, name='category'),
	url(r'^user_profile/(?P<u_id>[\w\-]+)/$', views.user_profile, name='user_profile'),
	url(r'^add_reply/(?P<post_id>[\w\-]+)-(?P<comment_id>[\w\-]+)/', views.add_reply, name='add_reply'),
	url(r'^edit_post/(?P<post_id>[\w\-]+)/', views.edit_post, name='edit_post'),

	url(r'^delete_comment/(?P<post_id>[\w\-]+)-(?P<comment_id>[\w\-]+)/$', views.delete_comment, name='delete_comment'),
	url(r'^delete_post/(?P<post_id>[\w\-]+)/', views.delete_post, name='delete_post'),
	url(r'^delete_reply/(?P<post_id>[\w\-]+)-(?P<reply_id>[\w\-]+)/$', views.delete_reply, name='delete_reply'),
	


	url(r'^posts/(?P<page_no>[\w\-]+)/', views.posts_list, name='posts_list'),
	
] 

