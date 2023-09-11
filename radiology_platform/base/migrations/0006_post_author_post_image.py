# Generated by Django 4.1.6 on 2023-05-23 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_delete_mailmessage'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(null=True, upload_to='blog_images/'),
        ),
    ]
