from django.contrib import admin

from blog.models import UserProfile, Posts, Category

class UserProfileAdmin(admin.ModelAdmin):

	list_display=('user','profession', 'birthdate', 'lives_in','profile_picture')
	search_fields=['user']

admin.site.register(UserProfile, UserProfileAdmin)


class CategoryAdmin(admin.ModelAdmin):

	list_display=('name',)
	search_fields=['name']
	
admin.site.register(Category, CategoryAdmin)


class PostsAdmin(admin.ModelAdmin):

	list_display=('title', 'category', 'likes', 'views', 'stars')
	search_fields=['title']
	

admin.site.register(Posts, PostsAdmin)



