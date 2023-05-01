from django.db import models
from account.models import User
# Create your models here.
class Patient(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField(null=True)
    cin_number = models.IntegerField(null=True)
    consultation_date = models.DateField(auto_now_add=True)
    Notes = models.TextField(default='' ,null=True)
    def get_patient_name(self):
        return f'{self.firstname} {self.lastname}'



   
class Report(models.Model):
    STATUS_CHOICES = (
        ('R', 'Requested'),
        ('P', 'In process'),
        ('V', 'Reviewed'),
        ('C', 'Completed'),
    )

    BODY_PART_CHOICES = (
        ('head', 'Head'),
        ('chest', 'Chest'),
        ('abdomen', 'Abdomen'),
        ('pelvis', 'Pelvis'),
        ('extremities', 'Extremities'),
        ('spine', 'Spine'),
    )

    EXAM_TYPE_CHOICES = (
        ('x-ray', 'X-ray'),
        ('mri', 'MRI'),
    )

    URGENCY_CHOICES = (
        ('U', 'Urgent'),
        ('N', 'Normal'),
        ('L', 'Low'),
    )

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateField()
    exam_type = models.CharField(max_length=100, choices=[('x-ray', 'X-Ray'), ('mri', 'MRI')])
    body_part = models.CharField(max_length=100, choices=BODY_PART_CHOICES)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    urgency = models.CharField(max_length=1, choices=URGENCY_CHOICES)
    doctor = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, related_name='doctor_reports')
    radiologist = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, related_name='reports_radiologist')
    details = models.TextField(default='' ,null=True)
    report_file = models.FileField(upload_to='reports/', null=True, blank=True)

    def get_patient_name(self):
        return self.patient.name if self.patient else ''

    # Getter for exam type display name
    def get_exam_type_display_name(self):
        return dict(self.EXAM_TYPE_CHOICES).get(self.exam_type, '')

    # Getter for body part display name
    def get_body_part_display_name(self):
        return dict(self.BODY_PART_CHOICES).get(self.body_part, '')

    # Getter for status display name
    def get_status_display_name(self):
        return dict(self.STATUS_CHOICES).get(self.status, '')

    # Getter for urgency display name
    def get_urgency_display_name(self):
        return dict(self.URGENCY_CHOICES).get(self.urgency, '')

    # Getter for doctor's name
    def get_doctor_name(self):
        return self.doctor.name if self.doctor else ''

    # Getter for radiologist's name
    def get_radiologist_name(self):
        return self.radiologist.name if self.radiologist else ''
    
    def get_details(self):
        return self.details