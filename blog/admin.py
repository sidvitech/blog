from django.contrib import admin

from blog.models import UserProfile, Posts, Category, PostData, CommentData, ReplyData

class UserProfileAdmin(admin.ModelAdmin):

	list_display=('user','profession', 'birthdate', 'lives_in','profile_picture')
	search_fields=['user']

admin.site.register(UserProfile, UserProfileAdmin)


class CategoryAdmin(admin.ModelAdmin):

	list_display=('name', 'total_posts')
	search_fields=['name']
	
admin.site.register(Category, CategoryAdmin)


class PostsAdmin(admin.ModelAdmin):

	list_display=('title', 'category', 'likes', 'views', 'stars', 'total_comments')
	search_fields=['title']
	
admin.site.register(Posts, PostsAdmin)


class PostDataAdmin(admin.ModelAdmin):

	list_display=('user','post_title', 'like', 'view', 'star')
	search_fields=['user']

admin.site.register(PostData, PostDataAdmin)


class CommentDataAdmin(admin.ModelAdmin):

	list_display=('user','post_title', 'comment', 'likes')
	search_fields=['user']

admin.site.register(CommentData, CommentDataAdmin)


class ReplyDataAdmin(admin.ModelAdmin):

	list_display=('user','post_title', 'comment', 'reply')
	search_fields=['user']

admin.site.register(ReplyData, ReplyDataAdmin)



