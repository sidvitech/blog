from django.conf.urls import url
from category.views import (
category, 
category_delete,

)


urlpatterns = [
    url(r'^category/', category, name="category"),
    url(r'^category_delete/', category_delete, name="category_delete"),

]
