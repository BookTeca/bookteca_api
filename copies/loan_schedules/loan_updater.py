import logging

from django.conf import settings
from django.core.mail import send_mail

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore, register_events
from apscheduler.triggers.cron import CronTrigger
from .loan_jobs import overdue_loans_notifications, return_reminders, unblocked_users, test
from datetime import datetime as dt, timedelta as td, date
from dateutil import zoneinfo, tz


today = dt.now().date()
yesterday = today - td(days=1)
tomorow = today + td(days=1)


def loan_job():
    
    unblocked_users()
    send_mail(
        f"Lembrete de devolução - {today}",
        f"Tá chegando a hora de devolver os seguintes livros livro seguido: ... na data de {today + td(days=1)}",
        settings.EMAIL_HOST_USER,
        ["vivy.saribeiro@gmail.com"],
        fail_silently=False
    )
    print("Email enviado!")


def start():
    sched = BackgroundScheduler()
    sched.add_jobstore(DjangoJobStore(), "default")
    sched.add_job(loan_job, trigger=CronTrigger(day_of_week="mon-fri", hour="9-16/2", minute="30", timezone=tz.UTC), jobstore="default", id="loan_job", replace_existing=True)
    register_events(sched)
    # sched.start()
