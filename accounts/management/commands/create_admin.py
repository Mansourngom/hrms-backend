import os
from django.core.management.base import BaseCommand
from accounts.models import User


class Command(BaseCommand):
    help = "Cree un superuser automatiquement depuis les variables d'environnement"

    def handle(self, *args, **kwargs):
        username = os.getenv('DJANGO_SUPERUSER_USERNAME')
        email = os.getenv('DJANGO_SUPERUSER_EMAIL')
        password = os.getenv('DJANGO_SUPERUSER_PASSWORD')

        if not username or not password:
            self.stdout.write("Variables DJANGO_SUPERUSER_* manquantes, skip.")
            return

        if User.objects.filter(username=username).exists():
            self.stdout.write(f"Superuser '{username}' existe deja.")
            return

        User.objects.create_superuser(
            username=username,
            email=email,
            password=password,
            role=User.Role.ADMIN,
        )
        self.stdout.write(self.style.SUCCESS(f"Superuser '{username}' cree avec succes."))