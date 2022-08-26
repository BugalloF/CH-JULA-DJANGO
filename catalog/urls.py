from django.urls import re_path 

from . import views


urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^users/$', views.PersonListView.as_view(), name='users'),
    re_path(r'^users/(?P<pk>\d+)$', views.PersonDetailView.as_view(), name='person-detail'),
    re_path(r'^friendships/$', views.FriendshipsListView, name='friendships'),
]