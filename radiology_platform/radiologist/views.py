from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect,get_object_or_404

from django.contrib import messages
from django.contrib.auth import logout
from django.db.models import Q
from .forms import PatientForm,ReportForm,AppointmentForm
from doctor.models import Patient,User,Report
from .models import Appointment
from  .decorators import radiologist_required
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.db.models import Case, When,Value,IntegerField



# Create your views here.
@radiologist_required
def radiologistHomeView(request):
    return render (request,'radiologist/dashboard.html')


@radiologist_required
def appointmentsView(request):
    appointments = Appointment.objects.filter(radiologist=request.user)

  
    return render(request, 'radiologist/appointments.html', {'appointments': appointments})

@radiologist_required
def confirm_delete(request, appointment_id):
    appointment = Appointment.objects.get(id=appointment_id)
    context = {'appointment': appointment}
    return render(request, 'radiologist/confirm_delete.html', context)

@radiologist_required
def delete_appointment(request, appointment_id):
    appointment = Appointment.objects.get(id=appointment_id)
    
    appointment.delete()
    return redirect('rad_appointments')

@radiologist_required    
def medical_history(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)
    reports = Report.objects.filter(patient=patient)
    context={'patient': patient, 'reports': reports}
    return render(request, 'radiologist/medical_history.html', context)


@radiologist_required    
def reportsView(request):
    reports = Report.objects.filter(radiologist=request.user).order_by(Case(
        When(urgency='U', then=Value(1)),
        When(urgency='N', then=Value(2)),
        When(urgency='L', then=Value(3)),
        default=Value(4),
        output_field=IntegerField(),
    )) 
       
    context = {
        'reports': reports,
    }    
    return render(request, 'radiologist/reports.html', context)



@radiologist_required  
def create_report(request):
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            report = form.save(commit=False)
            report.radiologist = request.user
            report.save()
    else:
        form = ReportForm()
    if 'HX-Request' in request.headers:    
        base_template = 'radiologist/create_report.html'
    else :
        base_template ='radiologist/reports.html'
    return render(request, base_template, {'form': form})


@radiologist_required    
def report_details(request, report_id):
    report = get_object_or_404(Report, id=report_id)
    if not('HX-Request' in request.headers):    
        return render(request, 'radiologist/reports.html')
    else:
        return render(request, 'radiologist/report_details.html',{'report':report})
    
    

@radiologist_required    
def create_appointment(request, report_id):
    report = get_object_or_404(Report, id=report_id)
    initial_values = {
    'email': report.patient.email,
    'exam_type': report.exam_type,
    'details': report.details,}
    form = AppointmentForm(initial=initial_values)
    if request.method == 'POST':
        form = AppointmentForm(request.POST, initial=initial_values)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.radiologist = report.radiologist
            appointment.patient = report.patient
            appointment.report = report
            appointment.body_part = report.body_part
            appointment.status = 'S'
            appointment.save()

    context = {
        'form': form,
        'report': report,
    }
    return render(request, 'radiologist/create_appointment.html', context)

@radiologist_required    
def update_appointment(request,appointment_id):
    if request.method == 'POST':
        appointment=Appointment.objects.get(id=appointment_id)
        report=appointment.report    
        form=AppointmentForm(request.POST,instance=appointment)
        if form.is_valid():
            form.save()
            print('valid')
            return HttpResponseRedirect(reverse_lazy('rad_appointments'))
        else :
            print(form.errors)    
    else:
        
        appointment=Appointment.objects.get(id=appointment_id)
        report=appointment.report   
        form=AppointmentForm(instance=appointment) 
    return render(request,'radiologist/update_appointment.html',{'form':form})

@radiologist_required    
def blogView(request):
    return render (request,'radiologist/addblog.html')
@radiologist_required    
def profileView(request,username):
    return render (request,'radiologist/profile.html')
@radiologist_required    
def notificationsView(request):
    return render (request,'radiologist/notifications.html')
@radiologist_required
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
    return render(request, 'radiologist/create_patient_form.html', {'form': form})

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