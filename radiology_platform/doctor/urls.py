from django.urls import path
from . import views
from .views import doctorHomeView,patientsView,blogView,reportsView,notificationsView,profileView,create_patient,create_report,report_details,download_report,download_file
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('doctor/', views.doctorHomeView , name='doctor'),
    path('doctor/patients', views.patientsView , name='patients'),

    path('doctor/reports', views.reportsView, name='reports'),
    path('doctor/create_report/', views.create_report, name='create_report'),
    path('doctor/reportdetails/<int:report_id>/', views.report_details, name='report_details'),
    path('doctor/patients/<int:patient_id>/medical_history', views.medical_history, name='medical_history'),
    path('download/<path:file_name>/', download_file, name='download_file'),    
    path('download/<int:report_id>/', views.download_report, name='download_report'),
    path('doctor/blog', views.blogView , name='addblog'),
    path('doctor/profile/<str:username>/', views.profileView, name='profil'),
    path('doctor/notifications', views.notificationsView , name='notifications'),
    path('doctor/createpatient', views.create_patient , name='create_patient'),
    
        ]