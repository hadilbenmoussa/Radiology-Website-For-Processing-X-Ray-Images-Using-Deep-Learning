from django.apps import AppConfig


class RadiologistConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'radiologist'

    def ready(self):
        # Import your signal function
        from .signals import send_appointment_email,send_appointment_updated_email
        from django.db.models.signals import post_save

        # Connect the signal to the Appointment model's post_save signal
        from .models import Appointment
        post_save.connect(send_appointment_email, sender=Appointment)
        post_save.connect(send_appointment_updated_email, sender=Appointment)


