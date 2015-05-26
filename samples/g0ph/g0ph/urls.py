from django.conf.urls import patterns, include, url
from django.contrib import admin

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
