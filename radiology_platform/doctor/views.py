from django.shortcuts import render,redirect
from .forms import PatientForm


# Create your views here.
def doctorHomeView(request):
    return render (request,'doctor/dashboard.html')
def patientsView(request):
    return render (request,'doctor/patients.html')
def reportsView(request):
    return render (request,'doctor/reports.html')
def blogView(request):
    return render (request,'doctor/blog.html')
def profilView(request):
    return render (request,'doctor/profile.html')
def notificationsView(request):
    return render (request,'doctor/notifications.html')



def create_patient(request):
    if not request.session.get('access_granted'):
        # Redirect the user to a page indicating that they need to click the "Add Patient" button first
        return redirect('doctor/access_denied')
    else:
        if request.method == 'POST':
            form = PatientForm(request.POST)
            print('form recived')
            if form.is_valid():
                print('form recived')
                form.save()
                return redirect('patients')
        else:
            form = PatientForm()
            return render(request, 'doctor/create_patient_form.html', {'form': form})
  
def add_patient(request):
    # Set a session variable to indicate that the user has clicked the button
    request.session['access_granted'] = True
    # Redirect the user to the create_patient URL
    return redirect('create_patient')
def access_denied(request):
    return render(request, 'doctor/access_denied.html')    
     