from django.contrib import admin
from .models import userprof, profilepic, UserProfile
# Register your models here.

admin.site.register(UserProfile)

admin.site.register(profilepic)
admin.site.register(userprof)