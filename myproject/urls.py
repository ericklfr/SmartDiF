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
from urllib.parse import urlencode
from django.http import HttpResponse
from django.contrib import admin
from django.conf.urls.static import static
from analisador import views


urlpatterns=[
    	url(r'^$',views.home, name='SmartDiF'),
	url(r'^sobre$',views.sobre, name='sobre'),
	url(r'^loading$',views.loading, name='loading'),
	url(r'^tecnicas_ativas$',views.tecnicas_ativas, name='tecnicas_ativas'),
	url(r'^finish/$', views.finish, name='finish'),
	url(r'^finishall/$', views.finishAll, name='finishall'),
	url(r'^dispatcher/$', views.dispatcher,name='dispatcher'),
	url(r'^admin/', include(admin.site.urls))] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

