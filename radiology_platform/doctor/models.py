from django.db import models

# Create your models here.
class Patient(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField(null=True)
    cin_number = models.IntegerField(null=True)
    consultation_date = models.DateField(auto_now_add=True)



    def __str__(self):
        return f'{self.firstname} {self.lastname}'
    
    