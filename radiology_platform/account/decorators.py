from django.core.exceptions import PermissionDenied
from django.shortcuts import render,redirect
from django.contrib import messages



def redirect_home(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_doctor:
            # Redirect authenticated doctors to the doctor home page
            return redirect('doctor')
        elif request.user.is_authenticated and request.user.is_radiologist:
            # Redirect authenticated doctors to the radiologist home page
            return redirect('radiologist')    
        elif request.user.is_authenticated and request.user.is_patient:
            # Redirect authenticated doctors to the patient home page
            return redirect('patient')    
        else:
            # For any other user, return the original view function
            return view_func(request, *args, **kwargs)

    return wrapper
def login_required_customized(view_func):

    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated :
            return view_func(request, *args, **kwargs)
        else :
            # Show a message to non-authenticated users trying to log out
            messages.error(request, 'You must be logged in to log out.')
            # Redirect the user to the home page or any other page
            return redirect('home')


    return wrapper


