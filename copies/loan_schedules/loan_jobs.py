from apscheduler.schedulers.background import BackgroundScheduler
from users.models import User
from copies.models import Copy, Loan
from datetime import datetime as dt, timedelta as td, date
from django.core.mail import send_mail
from django.conf import settings


today = dt.now().date()
yesterday = today - td(days=1)
tomorow = today + td(days=1)


def return_reminders():
    users_return_loans = User.objects.all().filter(borrowings_copies__return_date__isnull=True, borrowings_copies__estimated_return_date=tomorow)

    loans_tobe_return = Loan.objects.all().filter(return_date__isnull=True, estimated_return_date=tomorow)

    list_emails = []
    notifications = []

    if users_return_loans.exists() and loans_tobe_return:
        for user in set(users_return_loans):
            list_emails.append(user.email)
            notification = {"userId": user.pk}
            notification["loans"] = []
            for loan in loans_tobe_return:
                if loan.user.id == user.pk:
                    notification["loans"].append(loan.copy.book.title)

            notifications.append(notification)

    return [list_emails, notifications]


def overdue_loans_notifications():
    users_overdue_loans = User.objects.all().filter(borrowings_copies__return_date__isnull=True, borrowings_copies__estimated_return_date__gt=yesterday)

    overdue_loans = Loan.objects.all().filter(return_date__isnull=True, estimated_return_date__gt=yesterday)

    list_emails = []
    notifications = []

    if users_overdue_loans.exists():
        for user in set(users_overdue_loans):
            list_emails.append(user.email)
            notification = {"userId": user.pk}
            notification["loans_pending"] = []
            for loan in overdue_loans:
                if loan.user.id == user.pk:
                    notification["loans_pending"].append(loan.copy.book.title)

            notifications.append(notification)

    return [list_emails, notifications]


def unblocked_users():
    users_blocked = User.objects.all().filter(is_blocked=True, blocked_until=yesterday)

    if users_blocked.exists():
        for user in users_blocked:
            user.is_blocked = False
            user.blocked_until = None

    User.objects.bulk_update(users_blocked, ["is_blocked", "blocked_until"])


def test():
    print(f"A data é {today}, a cada 1 min")