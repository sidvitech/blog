from django.contrib import admin
from post.models import Post, MyComment, Like

# Register your models here.


admin.site.register(Like)
admin.site.register(Post)
admin.site.register(MyComment)