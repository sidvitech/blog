from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from post.views import (
frontpage,
frontview,
mycomment,
commentview,
comment_delete,
delete_comment,
contact,
image,
)


urlpatterns = [
    url(r'^frontpage/', frontpage, name="frontpage"),
    url(r'^frontview/', frontview, name="frontview"),
    url(r'^mycomment/', mycomment, name="mycomment"),
    url(r'^commentview/', commentview, name="commentview"),
    url(r'^comment_delete/', comment_delete, name="comment_delete"),
    url(r'^delete_comment/(?P<pk>[0-9]+)', delete_comment, name="delete_comment"),
    url(r'^contact/', contact, name="contact"),
    url(r'^image/', image, name="image"),


]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)