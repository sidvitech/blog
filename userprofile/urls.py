from django.conf.urls import url
from userprofile.views import (
	update_profile,
	user_profile,
	)


urlpatterns = [
    url(r'^update_profile/', update_profile, name="update_profile"),
    url(r'^user_profile/', user_profile, name="user_profile"),
	]