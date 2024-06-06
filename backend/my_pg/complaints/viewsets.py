from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Complaint
from .serializers import ComplaintSerializer

class ComplaintViewSet(viewsets.ModelViewSet):
    queryset = Complaint.objects.all()
    serializer_class = ComplaintSerializer

    @action(detail=True, methods=['put', 'patch'])
    def assign(self, request, pk=None):
        complaint = self.get_object()
        complaint.assigned_staff_id = request.data.get('assigned_staff')
        complaint.save()
        return Response({'status': 'assigned'})

    @action(detail=True, methods=['put', 'patch'])
    def resolve(self, request, pk=None):
        complaint = self.get_object()
        complaint.status = 'resolved'
        complaint.resolution_details = request.data.get('resolution_details', '')
        complaint.save()
        return Response({'status': 'resolved'})
