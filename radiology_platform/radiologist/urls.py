from django.urls import path
from . import views
from .views import radiologistHomeView,appointmentsView,blogView,profileView,notificationsView,create_appointment,confirm_delete,delete_appointment,update_appointment
urlpatterns = [
    path('radiologist/', views.radiologistHomeView , name='radiologist'),
    path('radiologist/appointments', views.appointmentsView , name='rad_appointments'),
    path('radiologist/createpatient', views.create_patient , name='rad_create_patient'),
    path('radiologist/createappointment<int:report_id>', views.create_appointment , name='create_appointment'),
    path('radiologist/update_appointment/<int:appointment_id>/', views.update_appointment, name='update_appointment'),
    path('radiologist/appointments/<int:appointment_id>/delete/', views.delete_appointment, name='delete-appointment'),
    path('radiologist/appointments/<int:appointment_id>/confirm-delete/', views.confirm_delete, name='confirm-delete'),
    path('radiologist/create_report/', views.create_report, name='rad_create_report'),
    path('doctor/reportdetails/<int:report_id>/', views.report_details, name='rad_report_details'),
    path('radiologist/patients/<int:patient_id>/medical_history', views.medical_history, name='rad_medical_history'),

    path('radiologist/reports', views.reportsView , name='rad_reports'),
    path('radiologist/blog', views.blogView , name='rad_addblog'),
    path('radiologist/profile/<str:username>/', views.profileView, name='rad_profil'),
    path('radiologist/notifications', views.notificationsView , name='rad_notifications'),
    # path('radiologist/access_denied/', views.access_denied, name='access_denied'),
        ]
