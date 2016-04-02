from django.conf.urls import url
from post.views import (
frontpage,
frontview,
)


urlpatterns = [
    url(r'^frontpage/', frontpage, name="frontpage"),
    url(r'^frontview/', frontview, name="frontview"),


]
