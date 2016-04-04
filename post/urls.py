from django.conf.urls import include, url
from django.contrib import admin
from post import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	url(r'^$',views.post_view, name='posthome'),
	url(r'^postcreate/$',views.post_create,name = 'postcreate'),
	url(r'^commentcreate/$',views.comment_create, name= 'commentcreate'),
	url(r'^commentview/$',views.comment_view, name = 'commentview'),
	url(r'^commentedit/$',views.comment_edit, name='commentedit'),
	]
if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)		