# Generated by Django 4.1.6 on 2023-04-27 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_googleauthenticator'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_admin',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_customer',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_employee',
        ),
        migrations.AddField(
            model_name='user',
            name='is_doctor',
            field=models.BooleanField(default=False, verbose_name='Is doctor'),
        ),
        migrations.AddField(
            model_name='user',
            name='is_patient',
            field=models.BooleanField(default=False, verbose_name='Is patient'),
        ),
        migrations.AddField(
            model_name='user',
            name='is_radiologist',
            field=models.BooleanField(default=False, verbose_name='Is radiologist'),
        ),
    ]
