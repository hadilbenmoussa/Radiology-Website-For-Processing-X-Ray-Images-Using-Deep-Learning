from django.core.exceptions import PermissionDenied
from django.shortcuts import render

def doctor_required(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_doctor:
            return view_func(request, *args, **kwargs)
        else:
            raise PermissionDenied()
    return wrapper