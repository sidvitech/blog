from django.conf.urls import url
from userauth.views import (
user_registration, 
user_login, 
user_logout, 
main_page,
user_reset_password,
image
# password_change
)


urlpatterns = [
    url(r'^user_registration/', user_registration, name="user_registration"),
    url(r'^user_login/', user_login, name="user_login"),

    url(r'^logout/', user_logout, name="user_logout"),
    url(r'^main_page/', main_page, name="main_page"),
    url(r'^user_reset_password/', user_reset_password, name="user_reset_password"),
    url(r'^image/', image, name="image"),
    # url(r'^password_change/', password_change, name="password_change"),
    # url(r'^change_password/', auth_views.password_change, name="change_password"),

]
