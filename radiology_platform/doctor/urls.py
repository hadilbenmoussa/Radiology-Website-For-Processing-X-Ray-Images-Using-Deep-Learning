from django.urls import path
from . import views
from .views import doctorHomeView,patientsView,blogView,reportsView,notificationsView,profilView,create_patient,access_denied,add_patient

urlpatterns = [
    path('doctor/', views.doctorHomeView , name='doctor'),
    path('doctor/patients', views.patientsView , name='patients'),
    path('doctor/reports', views.reportsView , name='reports'),
    path('doctor/blog', views.blogView , name='blog'),
    path('doctor/profil', views.profilView , name='profil'),
    path('doctor/notifications', views.notificationsView , name='notifications'),
    path('doctor/createpatient', views.create_patient , name='create_patient'),
    path('doctor/add_patient/', views.add_patient, name='add_patient'),
    path('doctor/access_denied/', views.access_denied, name='access_denied'),
        ]