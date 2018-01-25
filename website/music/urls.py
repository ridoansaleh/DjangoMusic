from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.index), 
    url(r'^edit/song/?P<pk>\d+', views.editSong),
]