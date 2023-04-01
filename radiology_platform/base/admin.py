from django.contrib import admin
from .models import Post, MailMessage,Subscribers

# Register your models here.
admin.site.register(Post)
admin.site.register(Subscribers)
admin.site.register(MailMessage)