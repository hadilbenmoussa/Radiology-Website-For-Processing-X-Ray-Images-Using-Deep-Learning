from django.shortcuts import render

# Create your views here.
def radiologistHomeView(request):
    return render (request,'radiologist/home.html')