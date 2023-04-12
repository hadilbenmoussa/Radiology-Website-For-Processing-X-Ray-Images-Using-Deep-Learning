from django.urls import path
from . import views
from .views import patientHomeView

urlpatterns = [
    path('patient/', views.patientHomeView , name='patient'),]