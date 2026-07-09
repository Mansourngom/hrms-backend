from datetime import date
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions

from employees.models import Employee
from departments.models import Department
from attendance.models import Attendance
from leaves.models import LeaveRequest

from .serializers import DashboardStatsSerializer


class DashboardStatsView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        today = date.today()

        total_employees = Employee.objects.count()
        active_employees = Employee.objects.filter(status=Employee.Status.ACTIVE).count()
        archived_employees = Employee.objects.filter(status=Employee.Status.ARCHIVED).count()

        present_today = Attendance.objects.filter(
            date=today, status=Attendance.Status.PRESENT
        ).count()
        absent_today = Attendance.objects.filter(
            date=today, status=Attendance.Status.ABSENT
        ).count()

        on_leave_today = LeaveRequest.objects.filter(
            status=LeaveRequest.Status.APPROVED,
            start_date__lte=today,
            end_date__gte=today,
        ).count()

        pending_leave_requests = LeaveRequest.objects.filter(
            status=LeaveRequest.Status.PENDING
        ).count()

        total_departments = Department.objects.count()

        data = {
            'total_employees': total_employees,
            'active_employees': active_employees,
            'archived_employees': archived_employees,
            'present_today': present_today,
            'absent_today': absent_today,
            'on_leave_today': on_leave_today,
            'pending_leave_requests': pending_leave_requests,
            'total_departments': total_departments,
        }

        serializer = DashboardStatsSerializer(data)
        return Response(serializer.data)