from django.conf.urls import patterns, include, url
from django.contrib import admin
from lazyhelp import views
from lazyhelp import views as lazyhelp_views
from django.conf import settings  

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin', include(admin.site.urls)),
    url(r'^index$', views.index),
    url(r'^deal$', views.deal),
    url(r'^deal_build$', views.deal_build),
    url(r'^deal_map$', views.deal_map),
    url(r'^ad$', views.ad),
    url(r'^center$',views.center),
    url(r'^dispute$', views.dispute),
    url(r'^login$', views.login),
    url(r'^register$', views.register),
    url(r'^logout$', views.logout),
)
