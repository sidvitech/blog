from django.contrib import admin
from category.models import Category


# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'user_name')


admin.site.register(Category, CategoryAdmin)
