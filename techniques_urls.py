from django.conf.urls import url 
from httpproxy.views import HttpProxy

urlpatterns = [ 
url(r'^illuminants/(?P<url>.*)$',HttpProxy.as_view(base_url='http://127.0.0.1:26490/')),
]