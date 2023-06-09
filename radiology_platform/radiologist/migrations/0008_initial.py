# Generated by Django 4.1.6 on 2023-05-01 01:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('doctor', '0012_patient_notes_report'),
        ('radiologist', '0007_delete_appointment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_and_time', models.DateTimeField()),
                ('body_part', models.CharField(choices=[('head', 'Head'), ('chest', 'Chest'), ('abdomen', 'Abdomen'), ('pelvis', 'Pelvis'), ('extremities', 'Extremities'), ('spine', 'Spine')], max_length=100)),
                ('exam_type', models.CharField(choices=[('x-ray', 'X-ray'), ('mri', 'MRI')], max_length=100)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('details', models.TextField(default='', null=True)),
                ('status', models.CharField(choices=[('PENDING', 'Pending'), ('SCHEDULED', 'Scheduled')], default='PENDING', max_length=10)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor.patient')),
                ('radiologist', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='radiologist_reports', to=settings.AUTH_USER_MODEL)),
                ('report', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='doctor.report')),
            ],
        ),
    ]
