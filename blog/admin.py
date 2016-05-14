from django.contrib import admin

from blog.models import UserProfile, Posts, Category

class UserProfileAdmin(admin.ModelAdmin):

	list_display=('first_name', 'last_name', 'email')
	search_fields=['email']
	

admin.site.register(UserProfile, UserProfileAdmin)

class CategoryAdmin(admin.ModelAdmin):

	list_display=('name',)
	search_fields=['name']
	

admin.site.register(Category, CategoryAdmin)

class PostsAdmin(admin.ModelAdmin):

	list_display=('title', 'category', 'likes', 'views', 'stars')
	search_fields=['title']
	

admin.site.register(Posts, PostsAdmin)



