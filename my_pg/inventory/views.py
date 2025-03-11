# from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import InventoryItem, InventoryTransaction
from .serializers import InventoryItemSerializer, InventoryTransactionSerializer

class InventoryItemViewSet(viewsets.ModelViewSet):
    queryset = InventoryItem.objects.all()
    serializer_class = InventoryItemSerializer

class InventoryTransactionViewSet(viewsets.ModelViewSet):
    queryset = InventoryTransaction.objects.all()
    serializer_class = InventoryTransactionSerializer

    def get_queryset(self):
        if 'id' in self.kwargs:
            return self.queryset.filter(item_id=self.kwargs['id'])
        return self.queryset
