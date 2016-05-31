from django.conf.urls import patterns, include, url
from django.contrib import admin
from lazyhelp.views import here,index,deal,deal_build,ad,dispute,center
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
    url(r'^ad$', ad),
    url(r'^center$',center),
    url(r'^dispute$',dispute),
)
