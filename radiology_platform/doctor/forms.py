from django import forms
from .models import Patient

class PatientForm(forms.ModelForm):
    # firstname = forms.CharField(label='First Name', max_length=100)
    # lastname = forms.CharField(label='Last Name', max_length=100)
    # email = forms.EmailField(label='Email')
    # cin_number = forms.IntegerField(label='CIN Number')
    class Meta:
        model = Patient
        fields = ['firstname', 'lastname', 'email','cin_number']
    
  
   
