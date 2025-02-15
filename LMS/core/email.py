from django.core.mail import send_mail
from django.utils.timezone import now, timedelta
from LMS.LMS.settings import EMAIL_HOST_USER
from Transaction.models import Transaction

def send_due_notifications():
 
    thirty_days_ago = now() - timedelta(days=30)
    overdue_transactions = Transaction.objects.filter(transaction_type='borrow', date__lte=thirty_days_ago)

    for transaction in overdue_transactions:
        if not student_email:
            print(f"Skipping transaction {transaction.id}: No email found.")
        student_email = transaction.student.email  # Ensure Student model has an `email` field
        subject = "Library Book Return Reminder"
        message = f"""
        Dear {transaction.student_name},

        This is a reminder that you borrowed the book "{transaction.book_name}" on {transaction.date.strftime('%Y-%m-%d')}.
        Please return the book to the library as soon as possible to avoid penalties.

        Thank you,
        Library Management
        """
        send_mail(subject, message, EMAIL_HOST_USER, [student_email])


    print(f"Sent {overdue_transactions.count()} reminder emails.")
