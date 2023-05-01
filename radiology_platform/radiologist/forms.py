from django import forms
from doctor.models import Patient,Report
from .models import Appointment
from django.forms import DateTimeInput

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['email', 'exam_type', 'date_and_time', 'details']
        widgets = {
            'email': forms.EmailInput(attrs={'readonly': True}),
            'exam_type': forms.TextInput(attrs={'readonly': True}),
            'date_and_time':forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
        }




class PatientForm(forms.ModelForm):
    # firstname = forms.CharField(label='First Name', max_length=100)
    # lastname = forms.CharField(label='Last Name', max_length=100)
    # email = forms.EmailField(label='Email')
    # cin_number = forms.IntegerField(label='CIN Number')
    class Meta:
        model = Patient
        fields = ['firstname', 'lastname', 'email','cin_number']
    
class ReportForm(forms.ModelForm):
    patient = forms.ModelChoiceField(queryset=Patient.objects.all())

    class Meta:
        model = Report
        fields = ['patient', 'date','body_part','urgency' ,'exam_type','details']  
        widgets = {
            'exam_type': forms.Select(choices=Report.EXAM_TYPE_CHOICES),
            'body_part': forms.Select(choices=Report.BODY_PART_CHOICES),
                 'date': forms.DateInput(attrs={'type': 'date'})
        }
   
