from django.conf import settings
from django.db import models
from departments.models import Department


class Employee(models.Model):
    class Contract(models.TextChoices):
        CDI = 'CDI', 'CDI'
        CDD = 'CDD', 'CDD'
        STAGE = 'STAGE', 'Stage'
        FREELANCE = 'FREELANCE', 'Freelance'

    class Status(models.TextChoices):
        ACTIVE = 'ACTIVE', 'Actif'
        ARCHIVED = 'ARCHIVED', 'Archivé'

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='employee_profile',
        null=True,
        blank=True,
    )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    photo = models.ImageField(upload_to='employees/photos/', blank=True, null=True)

    department = models.ForeignKey(
        Department,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='employees',
    )
    position = models.CharField(max_length=100, blank=True, null=True)
    contract_type = models.CharField(max_length=20, choices=Contract.choices, default=Contract.CDI)
    hire_date = models.DateField()
    salary = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    status = models.CharField(max_length=20, choices=Status.choices, default=Status.ACTIVE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"