from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.db import transaction
from config.settings import deploy


class Command(BaseCommand):
    help = "Flush the database, load all necessary fixtures, and ensure integrity"

    def add_arguments(self, parser):
        parser.add_argument(
            "--noinput",
            action="store_true",
            help="Run the command without asking for user input.",
        )

    def handle(self, *args, **kwargs):
        noinput = kwargs.get("noinput", False)

        # Ask for confirmation if noinput flag is not set
        if not noinput:
            self.stdout.write(
                self.style.WARNING(
                    "This will flush the database and load new fixtures. This action is irreversible."
                )
            )

            self.stdout.write(
                self.style.WARNING(
                    f"deploy : {deploy}"
                )
            )

            confirm = input("Are you sure you want to proceed? (yes/no): ")
            if confirm.lower() != "yes":
                self.stdout.write(self.style.ERROR("Operation cancelled."))
                return
            
        
        call_command("migrate")


        try:
            with transaction.atomic():
                # Flush the database
                call_command("flush", "--noinput")

                # Load all required fixtures
                call_command("loaddata", "payment/fixtures/mock_payment.json")
                

            self.stdout.write(
                self.style.SUCCESS(
                    "Successfully flushed the database, loaded all fixtures, and ensured data integrity"
                )
            )

        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Error loading fixtures: {e}"))
