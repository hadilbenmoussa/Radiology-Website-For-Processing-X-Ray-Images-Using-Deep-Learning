from django.urls import path
from . import views
from .views import doctorHomeView,patientsView,blogView,reportsView,notificationsView,profilView,create_patient
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('doctor/', login_required(views.doctorHomeView) , name='doctor'),
    path('doctor/patients', login_required(views.patientsView) , name='patients'),
    path('doctor/reports', login_required(views.reportsView) , name='reports'),
    path('doctor/blog', login_required(views.blogView) , name='addblog'),
    path('doctor/profil', login_required(views.profilView) , name='profil'),
    path('doctor/notifications', login_required(views.notificationsView) , name='notifications'),
    path('doctor/createpatient', login_required(views.create_patient) , name='create_patient'),
    
        ]