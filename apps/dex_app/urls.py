from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r'^$', views.versionselect),
    url(r'^(?P<gen>[a-zA-Z0-9 -]+)/(?P<id>\d+)$', views.dex_page),
    url(r'^(?P<gen>[a-zA-Z0-9 -]+)$', views.pokedex),
    url(r'^moveshow$', views.moveshow),
    url(r'^moves$', views.moves)
]