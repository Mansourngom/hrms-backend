from rest_framework import viewsets, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Attendance
from .serializers import AttendanceSerializer


class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all().order_by('-date')
    serializer_class = AttendanceSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['employee', 'status', 'date']
    ordering_fields = ['date']