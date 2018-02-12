from django.conf.urls import url
from . import views
# from .views import HomeView

urlpatterns = [
    url(r'^$', views.index, name="index"), # function-based views
    # url(r'^$', HomeView.as_view(), name='home'), # class-based views
    url(r'^edit/(?P<pk>\d+)$', views.edit, name='edit'),
    url(r'^delete/(?P<pk>\d+)$', views.delete, name='delete'), 
    url(r'^login$', views.login, name='login'),
    url(r'^signup$', views.signup, name='signup'),
]