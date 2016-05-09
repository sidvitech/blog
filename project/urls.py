from django.conf.urls import url, include, patterns
from django.contrib import admin
from project import views
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^blog/', include('blog.urls', namespace='blog')),
    url(r'^$', views.home, name='home'),

]