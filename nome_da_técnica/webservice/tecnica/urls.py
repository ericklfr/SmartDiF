"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from somar import views
from httpproxy.views import HttpProxy
from api import views as views_api
from rest_framework.routers import SimpleRouter
from rest_framework.urlpatterns import format_suffix_patterns



urlpatterns=[
	url(r'^$',views.home, name='home'),
	url(r'^ilu$',views.ilu, name='ilu'),
	url(r'^finish/$', views.finish, name='finish'),
	url(r'^somar/$',views.somar, name='somar'),
	url(r'^test/(?P<entrypoint>[^/]+)/(?P<port>[^/]+)/$', views.somar,name='somar'),
	url(r'^subtrair/$', views.subtrair,name='somar'),
	url(r'^resultado/$',views.resultado,name='resultado')] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = format_suffix_patterns(urlpatterns)

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

