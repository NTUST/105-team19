from django.conf.urls import patterns, include, url
from django.contrib import admin
from lazyhelp.views import here, index, deal, deal_build, ad, deal_map, dispute, center, login, register,logout
from django.conf import settings  

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^here/$',here),
    url(r'^index$', index),
    url(r'^deal$', deal),
    url(r'^deal_build$', deal_build),
    url(r'^deal_map$', deal_map),
    url(r'^ad$', ad),
    url(r'^center$',center),
    url(r'^dispute$',dispute),
    url(r'^login$', login),
    url(r'^register$',register),
    url(r'^logout$',logout),
)
