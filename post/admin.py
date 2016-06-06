from django.contrib import admin
from post.models import Post, MyComment, Like, Reply, PostView

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'image')


admin.site.register(Like)
admin.site.register(Post, PostAdmin)
admin.site.register(MyComment)
admin.site.register(Reply)
admin.site.register(PostView)