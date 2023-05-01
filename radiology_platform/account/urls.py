from django.urls import path
from . import views

urlpatterns = [
path('login-register/', views.login_register, name='login_register'),
path('login/', views.login_view, name='login_view'),
path('user_type/', views.user_type, name='user_type'),
path('registermedical/<is_radiologist>/<is_doctor>/<is_patient>', views.register_medical, name='register_medical'),
path('registerpatient/<is_radiologist>/<is_doctor>/<is_patient>', views.register_patient, name='register_patient'),

path('logout/', views.logout_user, name='logout'),
]