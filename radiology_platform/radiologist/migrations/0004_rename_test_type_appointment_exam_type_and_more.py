# Generated by Django 4.1.6 on 2023-04-29 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('radiologist', '0003_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointment',
            old_name='test_type',
            new_name='exam_type',
        ),
        migrations.AlterField(
            model_name='appointment',
            name='date_and_time',
            field=models.DateField(),
        ),
    ]
