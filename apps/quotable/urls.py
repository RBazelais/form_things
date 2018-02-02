from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.landing, name="landing"),
    url(r'^process_quote$', views.process_quote)
]