from django import forms
from .models import Subscribers


class SubscribersForm(forms.ModelForm):
    class Meta:
        model = Subscribers
        fields = [
            "name",
            "email",
        ]


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
    phonenumber = forms.IntegerField()
