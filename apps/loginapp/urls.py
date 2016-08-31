from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^pokes$', views.success),
    url(r'^registration$', views.user),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
]