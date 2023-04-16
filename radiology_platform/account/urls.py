from django.urls import path
from . import views

urlpatterns = [
    path('login-register/',views.login_register,name='login_register'),
    path('login/', views.login_view, name='login_view'),
    path('user_type/', views.user_type, name='user_type'),

    path('register/<is_admin>/<is_customer>/<is_employee>', views.register, name='register'),
    path('adminpage/', views.admin, name='adminpage'),
    path('customer/', views.customer, name='customer'),
    path('employee/', views.employee, name='employee'),
    path('logout/', views.logout_user, name='logout'),
]