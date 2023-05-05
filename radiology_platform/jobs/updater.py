from django.apps import AppConfig
from apscheduler.schedulers.background import BackgroundScheduler
from .jobs import send_email_job,check_appointments



def start():
        scheduler = BackgroundScheduler()
        scheduler.add_job(check_appointments, 'interval', seconds=3000)
        scheduler.add_job(send_email_job, 'interval', days=7)
        scheduler.start()