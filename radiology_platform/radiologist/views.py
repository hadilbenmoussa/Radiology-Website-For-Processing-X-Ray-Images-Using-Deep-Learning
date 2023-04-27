from django.shortcuts import render
from .decorators import radiologist_required
# Create your views here.
def radiologistHomeView(request):
    return render (request,'radiologist/home.html')