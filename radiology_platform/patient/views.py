from django.shortcuts import render

from .decorators import patient_required
from radiologist.models import Appointment
from doctor.models import Patient, Report


# Create your views here.
@patient_required
def patientAppointments(request):
    # Get all appointments where the patient is the current user
    patient = Patient.objects.get(email=request.user.email)

    appointments = patient.appointment_set.all()

    return render(request, "patient/appointments.html", {"appointments": appointments})


@patient_required
def patientReports(request):
    currentpatient = Patient.objects.get(email=request.user.email)

    reports = Report.objects.filter(patient=currentpatient)

    return render(request, "patient/reports.html", {"reports": reports})


@patient_required
def patientprofileView(request, username):
    return render(request, "patient/profile.html")
