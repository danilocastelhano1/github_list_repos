from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Seed the database information"

    def create_super_user(self):
        if User.objects.count() == 0:
            self.stdout.write(
                self.style.WARNING("Starting the Super User Insertion process")
            )
            User.objects.create_superuser(
                "admin", "admin@example.com", "admin"
            )
            self.stdout.write(
                self.style.SUCCESS("Finalized Super User creation process")
            )

    def handle(self, *args, **options):
        self.create_super_user()
