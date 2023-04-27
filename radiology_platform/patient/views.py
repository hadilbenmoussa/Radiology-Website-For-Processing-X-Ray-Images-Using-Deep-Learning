from django.shortcuts import render
from .decorators import patient_required
# Create your views here.
@patient_required
def patientHomeView(request):
    return render (request,'patient/home.html')