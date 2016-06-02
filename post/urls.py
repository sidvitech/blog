from django.conf import settings
from django.conf.urls import url
from post.views import (
create_post,
post_list,
all_post,
gallery_image,
category_android,
category_education,
delete_comment,
post_detail,
)


urlpatterns = [
    url(r'^create_post/', create_post, name="create_post"),
    url(r'^post_list/', post_list, name="post_list"),
    url(r'^all_post/', all_post, name="all_post"),
    url(r'^gallery_image/', gallery_image, name="gallery_image"),
    url(r'^category_android/', category_android, name="category_android"),
    url(r'^category_education/', category_education, name="category_education"),
    url(r'^delete_comment/(?P<pk>[0-9]+)', delete_comment, name="delete_comment"),
    url(r'^(?P<pk>[0-9]+)/', post_detail, name="post_detail"),

]
