from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"), 
    url(r'^edit/(?P<pk>\d+)$', views.edit, name='edit_song'),
    url(r'^delete/(?P<pk>\d+)$', views.delete, name='delete'), 
]