# Generated by Django 4.1.6 on 2023-04-30 23:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('radiologist', '0006_appointment_radiologist_appointment_status'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Appointment',
        ),
    ]