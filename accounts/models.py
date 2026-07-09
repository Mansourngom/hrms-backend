from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = 'ADMIN', 'Administrateur'
        RH = 'RH', 'Responsable RH'
        MANAGER = 'MANAGER', 'Manager'
        EMPLOYEE = 'EMPLOYEE', 'Employé'
        COMPTABLE = 'COMPTABLE', 'Comptable'

    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.EMPLOYEE,
    )
    phone = models.CharField(max_length=20, blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"