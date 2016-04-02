from django.conf.urls import include, url
from django.contrib import admin
from category import views
from django.conf import settings


urlpatterns = [
	url(r'^$',views.category, name='home'),
	]