from django.conf.urls import url

from home import views


urlpatterns = [
    url(r'^$', views.Home.as_view(), name='home'),
    url(r'^create/group/$', views.CreateGroup.as_view(), name='create_group'),
    url(r'^view/groups/$', views.UserViewGroups.as_view(), name='user_view_groups'),
    url(r'^view/group/(?P<pk>\d+)/$', views.GroupDetail.as_view(), name='group_detail'),
    url(r'^view/group/(?P<pk>\d+)/create/event/$', views.CreateEvent.as_view(), name='create_event'),
    url(r'^view/group/event/(?P<pk>\d+)/$', views.EventDetail.as_view(), name='event_detail'),
    url(r'^groups/$', views.GroupList.as_view(), name='group_list'),
    url(r'^group/(?P<pk>\d+)/$', views.GuestGroupDetail.as_view(), name='guest_group_detail'),
]
