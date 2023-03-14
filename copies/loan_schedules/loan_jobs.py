from apscheduler.schedulers.background import BackgroundScheduler
from users.models import User
from models import Copy, Loan
from datetime import datetime as dt, timedelta as td


def loan_notifications():
    today = dt.now().date()
    users_overdue_loans = User.objects.filter(borrowings_copies__return_date__isnull=True, borrowings_copies__estimated_return_date__gt=today).all()
    list_emails = []
    # return_date__isnull=True, estimated_return_date__gt=today
    # Loan.objects.filter(return_date__isnull=True, estimated_return_date__gt=today).all()
    # users_overdue_loans
    if users_overdue_loans:
        for user in set(users_overdue_loans):
            list_emails.append(user.email)
