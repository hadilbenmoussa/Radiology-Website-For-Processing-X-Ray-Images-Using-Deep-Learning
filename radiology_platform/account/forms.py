from django.core.exceptions import ValidationError
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class LoginForm(forms.Form):
    username = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
class UserTypeForm(forms.Form):
    is_admin = forms.BooleanField(label='admin', required=False)
    is_customer = forms.BooleanField(label='customer', required=False)
    is_employee = forms.BooleanField(label='employee', required=False)
    
    
    
    
        



class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    def clean(self):
        cleaned_data = super().clean()
        is_admin = cleaned_data.get('is_admin')
        is_employee = cleaned_data.get('is_employee')
        is_customer = cleaned_data.get('is_customer')

        roles_selected = [is_admin, is_employee, is_customer]
        roles_selected_count = roles_selected.count(True)

        if roles_selected_count > 1:
            raise ValidationError("Please select only one user role.")

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')