from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^api/sample', include('sample_api.urls')),
    url(r'^admin/', admin.site.urls),
]
