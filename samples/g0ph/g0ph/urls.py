from django.conf.urls import patterns, include, url
from django.contrib import admin
from nucleo.views import UserList, UserDetail
from nucleo.views import PostList, PostDetail, UserPostList

# Configure django only for ADMIN and API.
urlpatterns = patterns(
    '',

    # g0ph API
    # url(r'^/g0ph-api/', include('g0ph.api.urls')),

    # See all-auth, rest-auth
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    url(r'^account/', include('allauth.urls')),

    # Admin
    url(r'^admin/', include(admin.site.urls)),
)

# Serve angular app with static files.
urlpatterns += patterns(
    'django.contrib.staticfiles.views',
    url(r'^(?:index.html)?$', 'serve', kwargs={'path': 'index.html'}),
    url(r'^(?P<path>(?:bower_components|views|scripts|styles|images)/.*)$', 'serve'),
)

user_urls = patterns('',
    url(r'^/(?P<username>[0-9a-zA-Z_-]+)/posts$', UserPostList.as_view(), name='userpost-list'),
    url(r'^/(?P<username>[0-9a-zA-Z_-]+)$', UserDetail.as_view(), name='user-detail'),
    url(r'^$', UserList.as_view(), name='user-list'),
)

post_urls = patterns('',
    url(r'^/(?P<pk>\d+)$', PostDetail.as_view(), name='post-detail'),
    url(r'^$', PostList.as_view(), name='post-list')
)

urlpatterns += patterns('',
    url(r'^api/users', include(user_urls)),
    url(r'^api/posts', include(post_urls)),
    url(r'^api/add_post$', 'nucleo.views.add_post', name='add_post'),
    url(r'^api/follow$', 'nucleo.views.follow', name='follow'),
)