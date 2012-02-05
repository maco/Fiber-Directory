from django.conf.urls.defaults import patterns, include, url
from fiberapp.views import HomeView
from fiberapp.views import FarmingView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$',HomeView.as_view(), name='home'),
    url(r'^service/farming$',FarmingView.as_view(), name='farming'),
    # url(r'^fiber/', include('fiber.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
