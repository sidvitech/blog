from django.conf.urls import url
from .views import (
user_registration, 
user_login, 
user_logout, 
main_page
)


urlpatterns = [
    url(r'^user_registration/', user_registration, name="user_registration"),
    url(r'^user_login/', user_login, name="user_login"),
    url(r'^user_logout/', user_logout, name="user_logout"),
    url(r'^main_page/', main_page, name="main_page"),

]
