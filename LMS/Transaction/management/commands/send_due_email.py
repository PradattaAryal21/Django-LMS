from django.core.management.base import BaseCommand
from core.email import send_due_notifications

class Command(BaseCommand):
    help = 'Send reminder emails to students who borrowed books more than 30 days ago'

    def handle(self, *args, **kwargs):
        send_due_notifications()
        self.stdout.write(self.style.SUCCESS("Reminder emails sent successfully"))
