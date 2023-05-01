from django.db import models
import pyotp
from django.contrib.auth.models import AbstractUser,Group,Permission
# Create your models here.


class User(AbstractUser):
    
    is_radiologist= models.BooleanField('Is radiologist', default=False)
    is_doctor = models.BooleanField('Is doctor', default=False)
    is_patient = models.BooleanField('Is patient', default=False)
    cin_number=models.IntegerField('cin_number',default=0000000)
class GoogleAuthenticator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    secret_key = models.CharField(max_length=16) 
    def get_otp_uri(self):
        totp = pyotp.TOTP(self.secret_key)
        return totp.provisioning_uri(self.user.email)