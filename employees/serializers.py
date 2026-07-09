from rest_framework import serializers
from .models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    department_name = serializers.SerializerMethodField()

    class Meta:
        model = Employee
        fields = [
            'id', 'user', 'first_name', 'last_name', 'email', 'phone', 'address',
            'photo', 'department', 'department_name', 'position', 'contract_type',
            'hire_date', 'salary', 'status', 'created_at', 'updated_at',
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']

    def get_department_name(self, obj):
        return obj.department.name if obj.department else None