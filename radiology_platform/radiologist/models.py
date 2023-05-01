
from django.db import models
from doctor.models import Patient,Report
from account.models import User
class Appointment(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('SCHEDULED', 'Scheduled'),
    ]
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    report = models.OneToOneField(Report, on_delete=models.CASCADE)
    date_and_time = models.DateTimeField()
    body_part = models.CharField(max_length=100, choices=Report.BODY_PART_CHOICES)
    exam_type = models.CharField(max_length=100, choices=Report.EXAM_TYPE_CHOICES)
    email = models.EmailField(null=True)
    details = models.TextField(default='', null=True)
    radiologist = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, related_name='radiologist_reports')

    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDING')

    def __str__(self):
        return f'Appointment for {self.patient} on {self.date_and_time}'
