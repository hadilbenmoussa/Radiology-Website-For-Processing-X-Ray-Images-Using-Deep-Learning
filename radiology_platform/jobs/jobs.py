import datetime
import pytz

from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail
from django.utils import timezone

from base.models import Subscribers,Post
from radiologist.models import Appointment
def send_email_job():
    subscribers = Subscribers.objects.all()
  # Get the latest articles from the database
    latest_articles = Post.objects.order_by('-created')[:6]
    context = {'latest_articles': latest_articles}


    for subscriber in subscribers:
            html_message = render_to_string('base/email_newsletter.html',context)
            plain_message = strip_tags(html_message)
            subject = 'New article alert'
            from_email = 'radioai.contact@gmail.com'
            recipient_list = [subscriber.email,]

            send_mail(
            subject,
            plain_message,
            from_email,
            recipient_list,
            html_message=html_message,
            fail_silently=False,
        )
def check_appointments():
    print('hey')
    now=timezone.now()
    str_now = timezone.now().strftime('%Y-%m-%d %H:%M:%S%z')
    now_with_timezone = f'{str_now[:-2]}:{str_now[-2:]}' # Combine formatted time and timezone offset
    

        
    appointments = Appointment.objects.filter(date_and_time__lt =now_with_timezone)
    print(f"Number of expired appointments: {len(appointments)}")

    for appointment in appointments:
         appointment.status='EXPIRED'  
         appointment.save()
         print(appointment.status)
