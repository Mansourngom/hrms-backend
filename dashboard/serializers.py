from rest_framework import serializers


class DashboardStatsSerializer(serializers.Serializer):
    total_employees = serializers.IntegerField()
    active_employees = serializers.IntegerField()
    archived_employees = serializers.IntegerField()
    present_today = serializers.IntegerField()
    absent_today = serializers.IntegerField()
    on_leave_today = serializers.IntegerField()
    pending_leave_requests = serializers.IntegerField()
    total_departments = serializers.IntegerField()