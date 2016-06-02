from django.conf.urls import url
from userauth.views import (
	user_registration, 
	user_login, 
	user_logout, 
	user_reset_password,
	
	)


urlpatterns = [
    url(r'^user_registration/', user_registration, name="user_registration"),
    url(r'^user_login/', user_login, name="user_login"),
    url(r'^user_logout/', user_logout, name="user_logout"),
    url(r'^user_reset_password/', user_reset_password, name="user_reset_password"),
	]