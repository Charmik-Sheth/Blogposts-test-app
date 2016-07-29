from django.conf.urls import url
from . import views

urlpatterns = [url(r'^$', views.login_page, name='login_page'),
			   url(r'^new_login/$', views.new_login, name='new_login'),
			   url(r'^logout/(?P<user_id>[0-9]+)/$', views.logout, name='logout'),
			   url(r'^index/(?P<user_id>[0-9]+)/$', views.index, name='index'),
			   url(r'^new_post/(?P<user_id>[0-9]+)/$', views.new_post, name='new_post'),
			   url(r'^(?P<post_id>[0-9]+)/(?P<user_id>[0-9]+)/$', views.comment, name='comment'),
			   url(r'^(?P<post_id>[0-9]+)/(?P<user_id>[0-9]+)/new_comment/$', views.new_comment, name='new_comment'),
]