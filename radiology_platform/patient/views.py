from django.shortcuts import render

# Create your views here.
def patientHomeView(request):
    return render (request,'patient/home.html')