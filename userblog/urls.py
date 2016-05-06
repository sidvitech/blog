from django.conf.urls import url
from userblog.views import (
blog,
blog_delete,

)


urlpatterns = [
    url(r'^blog/', blog, name="blog"),
    url(r'^blog_delete/', blog_delete, name="blog_delete"),


]
