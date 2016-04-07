from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from post.views import (
frontpage,
frontview,
mycomment,
commentview,
comment_delete,
)


urlpatterns = [
    url(r'^frontpage/', frontpage, name="frontpage"),
    url(r'^frontview/', frontview, name="frontview"),
    url(r'^mycomment/', mycomment, name="mycomment"),
    url(r'^commentview/', commentview, name="commentview"),
    url(r'^comment_delete/', comment_delete, name="comment_delete"),


]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)