from rest_framework import viewsets, permissions, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import LeaveRequest
from .serializers import LeaveRequestSerializer


class LeaveRequestViewSet(viewsets.ModelViewSet):
    queryset = LeaveRequest.objects.all().order_by('-created_at')
    serializer_class = LeaveRequestSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['employee', 'status', 'leave_type']
    ordering_fields = ['start_date', 'created_at']

    @action(detail=True, methods=['post'])
    def approve(self, request, pk=None):
        leave = self.get_object()
        leave.status = LeaveRequest.Status.APPROVED
        leave.comment = request.data.get('comment', '')
        leave.save()
        return Response(self.get_serializer(leave).data)

    @action(detail=True, methods=['post'])
    def reject(self, request, pk=None):
        leave = self.get_object()
        leave.status = LeaveRequest.Status.REJECTED
        leave.comment = request.data.get('comment', '')
        leave.save()
        return Response(self.get_serializer(leave).data)