from django.conf.urls import url, include, patterns
from django.contrib import admin
from project import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views

urlpatterns = [
	url(r'^$', views.home, name='home'),
	url(r'^admin/', admin.site.urls),
	url(r'^blog/', include('blog.urls', namespace='blog')),
	url(r'^login/$', auth_views.login),	
	url(r'^password_reset/$', auth_views.password_reset , {'post_reset_redirect':'/password_reset_done'}),
	url(r'^password_reset_done/$', auth_views.password_reset_done),
	url(r'^password_reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>[0-9A-Za-z]{1,3}-[0-9A-Za-z]{1,20})/$', auth_views.password_reset_confirm, {'post_reset_redirect': '/password_done/' }),
	url(r'^password_done/$', auth_views.password_reset_complete),
	url(r'^lock/$', views.lock, name='lock'),
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


