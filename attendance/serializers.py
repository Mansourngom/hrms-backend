from rest_framework import serializers
from .models import Attendance


class AttendanceSerializer(serializers.ModelSerializer):
    employee_name = serializers.SerializerMethodField()

    class Meta:
        model = Attendance
        fields = [
            'id', 'employee', 'employee_name', 'date', 'check_in', 'check_out',
            'status', 'note', 'created_at',
        ]
        read_only_fields = ['id', 'created_at']

    def get_employee_name(self, obj):
        return str(obj.employee)