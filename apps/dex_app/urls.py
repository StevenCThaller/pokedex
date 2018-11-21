from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r'^$', views.versionselect),
    url(r'^(?P<version>[a-zA-Z0-9 -]+)/(?P<id>\d+)$', views.dex_page),
    url(r'^$', views.pokedex),
    url(r'^show$', views.pokedexshow),
]