from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"), 
    url(r'^edit/(?P<pk>\d+)$', views.edit, name='edit'),
    url(r'^delete/(?P<pk>\d+)$', views.delete, name='delete'), 
    url(r'^login$', auth_views.login, {'template_name': 'music/login.html'}, name='login'),
    url(r'^signup$', views.signup, name='signup'),
]