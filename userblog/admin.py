from django.contrib import admin
from userblog.models import Blog


# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_display = ('blog_name', 'developer_name', )


admin.site.register(Blog, BlogAdmin)
