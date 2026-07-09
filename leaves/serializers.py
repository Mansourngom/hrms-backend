from rest_framework import serializers
from .models import LeaveRequest


class LeaveRequestSerializer(serializers.ModelSerializer):
    employee_name = serializers.SerializerMethodField()
    duration_days = serializers.IntegerField(read_only=True)

    class Meta:
        model = LeaveRequest
        fields = [
            'id', 'employee', 'employee_name', 'leave_type', 'start_date', 'end_date',
            'reason', 'status', 'comment', 'reviewed_by', 'duration_days',
            'created_at', 'updated_at',
        ]
        read_only_fields = ['id', 'status', 'reviewed_by', 'created_at', 'updated_at']

    def get_employee_name(self, obj):
        return str(obj.employee)