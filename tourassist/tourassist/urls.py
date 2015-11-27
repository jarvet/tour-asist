"""tourassist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles import views as staticview
from myweb import views

urlpatterns = [
    #url(r'^admin/', include(admin.site.urls)),
    url(r'^logout/$', views.userLogout),
    url(r'^index/$', views.main),
    url(r'^showProfile/(?P<UID>\d+)$', views.showProfile),
    url(r'^editProfile/$', views.editProfile),
    url(r'^$', views.loginAndRegister),
    url(r'^addPlan/$', views.addPlan),
    url(r'^showPlan/(?P<ID>\d+)/$', views.showPlan),
    url(r'^showTeam/(?P<ID>\d+)/$', views.showTeam),
    url(r'^kick/(?P<TID>\d+)/(?P<UID>\d+)$', views.kick), 
#    url(r'^profile/$', views.userProfile),
]

urlpatterns += [
url(r'^static/(?P<path>.*)$', staticview.static.serve, {'document_root': settings.STATIC_ROOT}, name="static"),
url(r'^media/(?P<path>.*)$', staticview.static.serve, {'document_root': settings.MEDIA_ROOT}, name="media")
]