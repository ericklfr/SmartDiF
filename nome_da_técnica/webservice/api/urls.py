from rest_framework.routers import SimpleRouter
from api import views


router = SimpleRouter()


router.register(r'somarapi', views.SomarAPIViewSet)

urlpatterns = router.urls
