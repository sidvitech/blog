from django.contrib import admin

# Register your models here.
from .models import userauth,userprofile,category,blogapp,post
# Register your models here.
admin.site.register(userauth)
admin.site.register(userprofile)
admin.site.register(category)
admin.site.register(blogapp)
admin.site.register(post)