from rest_framework.routers import DefaultRouter
from .viewsets import RoomViewSet

router = DefaultRouter()
router.register(r'rooms', RoomViewSet, basename='room')

urlpatterns = router.urls
