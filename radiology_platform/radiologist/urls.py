from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views
from .views import radiologistHomeView,appointmentsView,blogView,profileView,notificationsView,create_appointment,delete_appointment,update_appointment,generate_report,delete_report,predictImage
urlpatterns = [
    path('radiologist/', views.radiologistHomeView , name='radiologist'),
    path('radiologist/appointments', views.appointmentsView , name='rad_appointments'),
    path('radiologist/createpatient', views.create_patient , name='rad_create_patient'),
    path('radiologist/createappointment<int:report_id>', views.create_appointment , name='create_appointment'),
    path('radiologist/update_appointment/<int:appointment_id>/', views.update_appointment, name='update_appointment'),
    path('radiologist/appointments/<int:appointment_id>/delete/', views.delete_appointment, name='delete-appointment'),
    path('radiologist/reports/<int:appointment_id>/delete/', views.delete_report, name='delete_report'),

    path('radiologist/generatereport<int:report_id>', views.generate_report , name='generate_report'),

    path('radiologist/create_report/', views.create_report, name='rad_create_report'),
    # path('doctor/reportdetails/<int:report_id>/', views.report_details, name='rad_report_details'),
    path('radiologist/patients/<int:patient_id>/medical_history', views.medical_history, name='rad_medical_history'),

    path('radiologist/reports', views.reportsView , name='rad_reports'),
    path('radiologist/blog', views.blogView , name='rad_addblog'),
    path('radiologist/profile/<str:username>/', views.profileView, name='rad_profil'),
    path('radiologist/notifications', views.notificationsView , name='rad_notifications'),
    path('predictImage',views.predictImage,name='predictImage'),
        ]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # path('radiologist/access_denied/', views.access_denied, name='access_denied'),
       
