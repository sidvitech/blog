from django.contrib import admin

from blog.models import UserProfile, Posts

class UserProfileAdmin(admin.ModelAdmin):

	list_display=('first_name', 'last_name', 'email')
	search_fields=['email']
	

admin.site.register(UserProfile, UserProfileAdmin)

class PostsAdmin(admin.ModelAdmin):

	list_display=('title', 'likes', 'views', 'stars')
	search_fields=['title']
	

admin.site.register(Posts, PostsAdmin)

