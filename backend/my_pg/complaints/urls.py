from rest_framework.routers import DefaultRouter
from .viewsets import ComplaintViewSet

router = DefaultRouter()
router.register(r'complaints', ComplaintViewSet, basename='complaint')

urlpatterns = router.urls
