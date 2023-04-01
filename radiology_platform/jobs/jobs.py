import datetime
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail
from base.models import Subscribers,Post
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
   
  