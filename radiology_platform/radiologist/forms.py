from django import forms
from doctor.models import Patient,Report
from .models import Appointment
from django.forms import DateTimeInput
from django.utils import timezone

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['email', 'exam_type', 'date_and_time', 'details']
        widgets = {
            'email': forms.EmailInput(attrs={'readonly': True}),
            'exam_type': forms.TextInput(attrs={'readonly': True}),
            'date_and_time':forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
        }
class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['email', 'exam_type', 'date_and_time', 'details']
        widgets = {
            'email': forms.EmailInput(attrs={'readonly': True}),
            'exam_type': forms.TextInput(attrs={'readonly': True}),
            'date_and_time': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
        }

    def clean_date_and_time(self):
        date_and_time = self.cleaned_data.get('date_and_time')
        if date_and_time and date_and_time < timezone.now():
            raise forms.ValidationError('Please select a date in the future')
        return date_and_time



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
   
class  ReportFileForm(forms.Form):
    # Field for image upload
    image = forms.ImageField(required=True)
    
    indications = forms.CharField(widget=forms.Textarea)
    AI_check = forms.BooleanField(label='AI Diagnosis', widget=forms.CheckboxInput(),required=False)
    findings = forms.CharField(widget=forms.Textarea)
    impression= forms.CharField(widget=forms.Textarea)
    recommendations = forms.CharField(widget=forms.Textarea)