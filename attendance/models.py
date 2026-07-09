from django.db import models
from employees.models import Employee


class Attendance(models.Model):
    class Status(models.TextChoices):
        PRESENT = 'PRESENT', 'Présent'
        ABSENT = 'ABSENT', 'Absent'
        LATE = 'LATE', 'Retard'
        HALF_DAY = 'HALF_DAY', 'Demi-journée'

    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        related_name='attendances',
    )
    date = models.DateField()
    check_in = models.TimeField(blank=True, null=True)
    check_out = models.TimeField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.PRESENT)
    note = models.CharField(max_length=255, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('employee', 'date')  # un seul pointage par employé par jour
        ordering = ['-date']

    def __str__(self):
        return f"{self.employee} - {self.date} ({self.status})"