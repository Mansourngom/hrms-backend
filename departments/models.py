from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    budget = models.DecimalField(max_digits=14, decimal_places=2, default=0)
    manager = models.ForeignKey(
        'employees.Employee',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='managed_departments',
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    @property
    def employee_count(self):
        return self.employees.count()