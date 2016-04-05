from django.contrib import admin
from userauth.models import UserRegistration, View

# Register your models here.
admin.site.register(View)
admin.site.register(UserRegistration)