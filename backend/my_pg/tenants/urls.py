from rest_framework.routers import DefaultRouter
from .viewsets import TenantViewSet

router = DefaultRouter()
router.register(r'tenants', TenantViewSet, basename='tenant')

urlpatterns = router.urls
