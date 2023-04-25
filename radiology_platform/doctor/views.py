from django.shortcuts import render,redirect
from django.contrib import messages
from django.db.models import Q
from .forms import PatientForm
from .models import Patient



# Create your views here.
def doctorHomeView(request):
    return render (request,'doctor/dashboard.html')
def patientsView(request):
    return render (request,'doctor/patients.html')
def reportsView(request):
    return render (request,'doctor/reports.html')
def blogView(request):
    return render (request,'doctor/blog.html')
def profilView(request):
    return render (request,'doctor/profile.html')
def notificationsView(request):
    return render (request,'doctor/notifications.html')

def create_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        print('form received')
        if form.is_valid():
            email = form.cleaned_data['email']
            cin_number = form.cleaned_data['cin_number']
            existing_patient = get_object_or_none(Patient, email=email,cin_number=cin_number)
            if existing_patient:
                messages.success(request,'Already registered')
            else:
                messages.success(request,'registration successful')
                form.save()

            return redirect('patients')
    else:
        form = PatientForm()
    return render(request, 'doctor/create_patient_form.html', {'form': form})
  
def get_object_or_none(model, email=None, cin_number=None, **kwargs):
    filter_condition = Q()
    if email is not None:
        filter_condition |= Q(email=email)
    if cin_number is not None:
        filter_condition |= Q(cin_number=cin_number)
    if kwargs:
        filter_condition &= Q(**kwargs)

    try:
        return model.objects.get(filter_condition)
    except model.DoesNotExist:
        return None    