from django.conf.urls import url, include # Notice we added include
from django.contrib import admin

urlpatterns = [
    url(r'^', include('apps.login.urls')),
    # url(r'^dashboard/', include('apps.dashboard.urls')),
    url(r'^admin/', admin.site.urls)
]
