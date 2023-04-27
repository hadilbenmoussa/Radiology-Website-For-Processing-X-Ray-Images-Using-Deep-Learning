from django.core.exceptions import PermissionDenied
from django.shortcuts import render

def patient_required(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_patient:
            return view_func(request, *args, **kwargs)
        else:
            raise PermissionDenied()
    return wrapper