from django.contrib.auth.models import AbstractUser, Group,Permission
from django.db import models


# Create your models here.
class Radiologist(AbstractUser):
    # Add any additional fields you want here
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    groups = models.ManyToManyField(Group, related_name='radiologists')
    user_permissions = models.ManyToManyField(Permission, related_name='radiologists')