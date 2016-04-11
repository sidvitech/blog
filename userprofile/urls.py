from django.conf.urls import include, url
from django.contrib import admin
from userprofile import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	url(r'^$',views.userprof_view, name='home'),
	url(r'^add_userprofile/$', views.adduserprof_view, name='adddetails'),
	url(r'^updateprofiles/$', views.updateuserprof_view, name='updateprofile'),
	url(r'^register/$',views.register, name='register'),
	url(r'^editprofile/$',views.edit_profile, name='editprofile'),
	url(r'^updatepic/$',views.update_pic, name='updatepic'),
	]
if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)	