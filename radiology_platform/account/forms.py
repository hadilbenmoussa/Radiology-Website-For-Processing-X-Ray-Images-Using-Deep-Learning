from django.core.exceptions import ValidationError
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class LoginForm(forms.Form):
    username = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter Username"

            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter Password"

            }
        )
    )
    otp = forms.CharField(max_length=6, widget=forms.TextInput(attrs={'autocomplete': 'off',"placeholder": "Enter OTP"}))

class UserTypeForm(forms.Form):
    is_radiologist = forms.BooleanField(label='Tonnarelli', required=False,
        widget=forms.CheckboxInput(attrs={
            'class': 'checkbox-input',
            'id': 'tonnarelli',
        })
    )
    is_doctor = forms.BooleanField(label='doctor', required=False ,        widget=forms.CheckboxInput(attrs={
            'class': 'checkbox-input',
            'id': 'spaghetti',
        })
    )
    is_patient = forms.BooleanField(label='patient', required=False,widget=forms.CheckboxInput(attrs={
            'class': 'checkbox-input',
            'id': 'fettuccine',
        }))
    
    def clean(self):
        cleaned_data = super().clean()
        is_radiologist = cleaned_data.get('is_radiologist')
        is_doctor = cleaned_data.get('is_doctor')
        is_patient = cleaned_data.get('is_patient')

        roles_selected = [is_radiologist , is_doctor, is_patient]
        roles_selected_count = roles_selected.count(True)

        if roles_selected_count > 1:
            raise ValidationError("Please select only one user role.")
    
    
    
        



class SignUpForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "first name"

            }
        )
    )
    last_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "last name"

            }
        )
    )
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter your Username"

            }
        )
    )
    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter your email"

            }
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter your password"

                
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Confirm your password"

            }
        )
    )

    accept_terms = forms.BooleanField(
        label='I accept the terms and conditions',
        required=True,
        widget=forms.CheckboxInput(
            attrs={
                "class": "form-check-input"
            }
        )
    )



    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2','accept_terms')
class PatientSignUpForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "first name"

            }
        )
    )
    last_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "last name"

            }
        )
    )
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter your Username"

            }
        )
    )
    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter your email"

            }
        )
    )
    cin_number = forms.IntegerField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter your CIN number"

            }
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter your password"

                
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Confirm your password"

            }
        )
    )

    accept_terms = forms.BooleanField(
        label='I accept the terms and conditions',
        required=True,
        widget=forms.CheckboxInput(
            attrs={
                "class": "form-check-input"
            }
        )
    )



    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email','cin_number' ,'password1', 'password2','accept_terms')        
