from django.conf.urls import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = [
    # url(r'^$', include('blog.urls')),
    url(r'^mysite.blog', include('blog.urls')),
    url(r'^', include('blog.urls')),
    url(r'^mysite.admin/', admin.site.urls),
]
