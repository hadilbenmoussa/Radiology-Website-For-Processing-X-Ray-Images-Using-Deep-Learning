# Generated by Django 4.1.6 on 2023-05-23 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0014_remove_patient_doctor_patient_age_patient_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='exam_type',
            field=models.CharField(choices=[('x-ray', 'X-Ray'), ('mri', 'MRI'), ('ct', 'CT Scan'), ('ultrasound', 'Ultrasound')], max_length=100),
        ),
    ]