from django.urls import path
from . import views

urlpatterns = [
    path('login-register/',views.login_register,name='login_register'),
    path('login/', views.login_view, name='login_view'),
    path('user_type/', views.user_type, name='user_type'),
    path('registermedical/<is_admin>/<is_customer>/<is_employee>', views.register_medical, name='register_medical'),
    path('registerpatient/<is_admin>/<is_customer>/<is_employee>', views.register_patient, name='register_patient'),
    path('adminpage/', views.admin, name='adminpage'),
    path('customer/', views.customer, name='customer'),
    path('employee/', views.employee, name='employee'),
    path('logout/', views.logout_user, name='logout'),
]