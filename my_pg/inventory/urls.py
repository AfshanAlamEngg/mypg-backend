from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import InventoryItemViewSet, InventoryTransactionViewSet

router = DefaultRouter()
router.register(r'inventory', InventoryItemViewSet)
router.register(r'inventory/transactions', InventoryTransactionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
