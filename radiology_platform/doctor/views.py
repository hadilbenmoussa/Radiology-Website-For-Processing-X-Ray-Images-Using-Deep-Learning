from django.shortcuts import render,redirect,get_object_or_404

from django.contrib import messages
from django.contrib.auth import logout
from django.db.models import Q
from .forms import PatientForm,ReportForm
from .models import Patient,User,Report
from  .decorators import doctor_required
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


# Create your views here.
@doctor_required
def doctorHomeView(request):
    return render (request,'doctor/dashboard.html')


@doctor_required
def patientsView(request):
    patients = Patient.objects.all()
    return render(request, 'doctor/patients.html', {'patients': patients})

@doctor_required    
def medical_history(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)
    reports = Report.objects.filter(patient=patient)
    context={'patient': patient, 'reports': reports}
    return render(request, 'doctor/medical_history.html', context)


@doctor_required    
def reportsView(request):
    reports = Report.objects.filter(doctor=request.user)
    return render(request, 'doctor/reports.html', {'reports': reports})
@doctor_required  
def create_report(request):
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            report = form.save(commit=False)
            report.doctor = request.user
            report.status='R'
            report.radiologist = User.objects.filter(is_radiologist=True).first()
            report.save()
    else:
        form = ReportForm()
    if 'HX-Request' in request.headers:    
        base_template = 'doctor/create_report.html'
    else :
        base_template ='doctor/reports.html'
    return render(request, base_template, {'form': form})


@doctor_required    
def report_details(request, report_id):
    report = get_object_or_404(Report, id=report_id)
    if not('HX-Request' in request.headers):    
        return render(request, 'doctor/reports.html')
    else:
        return render(request, 'doctor/report_details.html',{'report':report})




@doctor_required    
def blogView(request):
    return render (request,'doctor/addblog.html')
@doctor_required    
def profileView(request,username):
    return render (request,'doctor/profile.html')
@doctor_required    
def notificationsView(request):
    return render (request,'doctor/notifications.html')
@doctor_required
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

@login_required
def logout_user(request):
    logout(request)
    return redirect('login_view')
 
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