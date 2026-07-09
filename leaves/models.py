from django.db import models
from employees.models import Employee


class LeaveRequest(models.Model):
    class LeaveType(models.TextChoices):
        ANNUAL = 'ANNUAL', 'Congé annuel'
        SICK = 'SICK', 'Maladie'
        MATERNITY = 'MATERNITY', 'Maternité'
        PATERNITY = 'PATERNITY', 'Paternité'
        UNPAID = 'UNPAID', 'Sans solde'
        OTHER = 'OTHER', 'Autre'

    class Status(models.TextChoices):
        PENDING = 'PENDING', 'En attente'
        APPROVED = 'APPROVED', 'Approuvé'
        REJECTED = 'REJECTED', 'Refusé'

    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        related_name='leave_requests',
    )
    leave_type = models.CharField(max_length=20, choices=LeaveType.choices, default=LeaveType.ANNUAL)
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.PENDING)
    comment = models.TextField(blank=True, null=True)  # commentaire du validateur

    reviewed_by = models.ForeignKey(
        Employee,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='reviewed_leaves',
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def duration_days(self):
        return (self.end_date - self.start_date).days + 1

    def __str__(self):
        return f"{self.employee} - {self.leave_type} ({self.start_date} → {self.end_date})"