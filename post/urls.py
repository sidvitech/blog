from django.conf.urls import url
from post.views import (
frontpage,
frontview,
mycomment,
commentview,
)


urlpatterns = [
    url(r'^frontpage/', frontpage, name="frontpage"),
    url(r'^frontview/', frontview, name="frontview"),
    url(r'^mycomment/', mycomment, name="mycomment"),
    url(r'^commentview/', commentview, name="commentview"),


]
