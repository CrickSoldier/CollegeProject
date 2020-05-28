from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url, include

urlpatterns = [
    url('polls/', include('polls.urls')),
    url('admin/', admin.site.urls),
]