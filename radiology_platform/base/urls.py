from django.urls import path
from . import views

urlpatterns = [
    path('', views.home , name='home'),
    path('requestappointment/',views.requestappointment, name='requestappointment'),
    path('patientcare/', views.patientcare, name='patientcare'),
    path('newsletter/',views.newsletter, name='newsletter'),
    path('aboutus/',views.aboutus, name='aboutus'),
]
