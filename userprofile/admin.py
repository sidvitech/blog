from django.contrib import admin
from userprofile.models import UserProfile

# Register your models here.

class UserProfileAdmin(admin.ModelAdmin):
	list_display = ('user', 'profile_picture')


admin.site.register(UserProfile, UserProfileAdmin)