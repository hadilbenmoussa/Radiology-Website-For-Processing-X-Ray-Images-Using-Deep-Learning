from django.urls import path
from . import views
from .views import patientAppointments, patientReports, patientprofileView


urlpatterns = [
    path(
        "patient/appointments", views.patientAppointments, name="patient_appointments"
    ),
    path("patient/reports", views.patientReports, name="patient_reports"),
    path(
        "patient/profile/<str:username>/",
        views.patientprofileView,
        name="patient_profil",
    ),
]
