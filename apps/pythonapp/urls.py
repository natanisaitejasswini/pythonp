from django.conf.urls import url, include
from . import views
urlpatterns = [
	url(r'^poke/(?P<id>\d+)$', views.poke),
    url(r'^check$', views.check),
]