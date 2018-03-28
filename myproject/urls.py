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
import httplib2
from urllib.parse import urlencode
from django.http import HttpResponse
from django.contrib import admin
from django.conf.urls.static import static
from analisador import views
from api import views as views_api
from rest_framework.routers import SimpleRouter
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns=[
    	url(r'^$',views.home, name='home'),
	url(r'', include('techniques_urls')),
	url(r'^finish/(?P<name>[^/]+)/(?P<id>[^/]+)/$', views.finish, name='finish'),
	url(r'^dispatcher/(?P<name>[^/]+)$', views.dispatcher,name='dispatcher'),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^Iluminantes$', views.Iluminantes,name='iluminantes'),
    	url(r'^Atribuição de Autoria no Twitter$', views.Twitter,name='twitter'),
	url(r'^Detalhes$', views.Detalhes,name='detalhes'),
	url(r'^Novo_modelo$', views.Novo_modelo,name='novo_modelo'),
	url(r'^api/somarapi$', views_api.SomarApiResultado),] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = format_suffix_patterns(urlpatterns)

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

