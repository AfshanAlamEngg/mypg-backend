from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NotificationViewSet, NotificationSettingsView, NotificationHistoryView

router = DefaultRouter()
router.register(r'notifications', NotificationViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('notifications/settings/', NotificationSettingsView.as_view(), name='notification-settings'),
    path('notifications/history/', NotificationHistoryView.as_view(), name='notification-history'),
]
