from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^api/genres/(?P<num>[0-9]+)/average$', views.average_artist_json),
    url(r'^(?P<num>[0-9]+)/average', views.average_artist),
    url(r'^(?P<num>[0-9]+)/tracks', views.list_table),
    url(r'^', views.genre_list)
]