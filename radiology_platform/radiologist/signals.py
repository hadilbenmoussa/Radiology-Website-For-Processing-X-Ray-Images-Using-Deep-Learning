from django.core.mail import send_mail
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Appointment


# Define a signal to send an email when an appointment is created
@receiver(post_save, sender=Appointment)
def send_appointment_email(sender, instance, created, **kwargs):
    if created:
        send_mail(
            "Appointment Confirmation",
            "Dear {}, your appointment on {} has been confirmed.Please note that you will need to {} ".format(
                instance.patient.get_patient_name(),
                instance.date_and_time,
                instance.details,
            ),
            "sender@example.com",
            [instance.email],
            fail_silently=False,
        )


@receiver(post_save, sender=Appointment)
def send_appointment_updated_email(sender, instance, update_fields, **kwargs):
    if update_fields and "date_and_time" in update_fields:
        # Send an email to the patient when the appointment date and time is updated
        subject = "Appointment Update"
        message = f"Dear {instance.patient.get_patient_name()}, your appointment date and time has been updated to {instance.date_and_time}.,{instance.details}"
        from_email = "example@example.com"
        recipient_list = [instance.patient.email]
        send_mail(subject, message, from_email, recipient_list, fail_silently=False)


@receiver(post_delete, sender=Appointment)
def send_appointment_deleted_email(sender, instance, **kwargs):
    # Send an email to the patient when an appointment is deleted
    subject = "Appointment Cancellation"
    message = f"Dear {instance.patient.get_patient_name()}, your appointment on {instance.date_and_time} has been cancelled."
    from_email = "example@example.com"
    recipient_list = [instance.patient.email]
    send_mail(subject, message, from_email, recipient_list, fail_silently=False)
