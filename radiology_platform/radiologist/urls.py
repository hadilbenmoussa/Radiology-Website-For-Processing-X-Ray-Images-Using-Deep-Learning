from django.urls import path
from . import views
from .views import radiologistHomeView

urlpatterns = [
    path('radiologist/', views.radiologistHomeView , name='radiologist'),]