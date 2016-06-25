from django.conf.urls import url

from home import views


urlpatterns = [
    url(r'^$', views.Home.as_view(), name='home'),
    url(r'^create/group/$', views.CreateGroup.as_view(), name='create_group'),
]
