from django import forms
from .models import Patient, Report
from base.models import Post


class PatientForm(forms.ModelForm):
    # firstname = forms.CharField(label='First Name', max_length=100)
    # lastname = forms.CharField(label='Last Name', max_length=100)
    # email = forms.EmailField(label='Email')
    # cin_number = forms.IntegerField(label='CIN Number')
    class Meta:
        model = Patient
        fields = ["firstname", "lastname", "email", "cin_number", "gender", "age"]


class ReportForm(forms.ModelForm):
    patient = forms.ModelChoiceField(queryset=Patient.objects.all())

    class Meta:
        model = Report
        fields = ["patient", "date", "body_part", "urgency", "exam_type", "details"]
        widgets = {
            "exam_type": forms.Select(choices=Report.EXAM_TYPE_CHOICES),
            "body_part": forms.Select(choices=Report.BODY_PART_CHOICES),
            "date": forms.DateInput(attrs={"type": "date"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["patient"].label_from_instance = lambda obj: obj.get_patient_name()


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "body", "image"]
