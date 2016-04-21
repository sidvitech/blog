from django.conf.urls import url
from django.views.generic.edit import CreateView
from .forms import UserRegistrationForm
from userauth.views import (
user_login, 
user_logout, 
user_reset_password,
)


urlpatterns = [
    url('^display_user/', CreateView.as_view(
            template_name='userauth/html123.html',
            form_class=UserRegistrationForm,
            success_url='/'
    )),
    url('^register_user/', CreateView.as_view(
            template_name='userauth/user_registration_form.html',
            form_class=UserRegistrationForm,
            success_url='/'
    )),
    url(r'^user_login/', user_login, name="user_login"),
    url(r'^user_logout/', user_logout, name="user_logout"),
    url(r'^user_reset_password/', user_reset_password, name="user_reset_password"),

]
