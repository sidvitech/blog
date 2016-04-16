from django.conf.urls import include, url
from django.contrib import admin
from post import views
from django.conf import settings
from django.conf.urls.static import static

app_name='post'
urlpatterns = [
	url(r'^$',views.post_view, name='posthome'),
	url(r'^postcreate/$',views.post_create,name = 'postcreate'),
	url(r'^commentcreate/$',views.comment_create, name= 'commentcreate'),
	url(r'^commentview/$',views.comment_view, name = 'commentview'),
	url(r'^commentedit/$',views.comment_edit, name='commentedit'),
	url(r'^postlist/$',views.post_list, name='postlist'),
	url(r'^(?P<pk>[0-9]+)/$',views.post_detail, name='post_detail'),
	]
if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)		