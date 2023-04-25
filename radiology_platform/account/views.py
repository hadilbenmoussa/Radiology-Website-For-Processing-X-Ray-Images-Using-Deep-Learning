from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm,UserTypeForm
from django.contrib.auth import authenticate, login,logout
from doctor.models import Patient
from django.contrib import messages
from django.db.models import Q
# Create your views here.


def login_register(request):
    return render(request, 'login_register.html')

def logout_user(request):
    logout(request)
    return redirect('login_view')
def user_type(request):
    if request.method == 'POST':
        form = UserTypeForm(request.POST)
        if form.is_valid():
            is_admin = form.cleaned_data['is_admin']
            is_customer = form.cleaned_data['is_customer']
            is_employee = form.cleaned_data['is_employee']
            if (is_admin or is_employee) :
                return redirect('register_medical',is_admin=is_admin,is_customer=is_customer, 
                    is_employee=is_employee)
            elif is_customer:
                return redirect('register_patient',is_admin=is_admin,is_customer=is_customer, 
                    is_employee=is_employee)
          

            # Do something with the checkbox values...
    else:
        form = UserTypeForm()
    return render(request, 'account/user_type.html',{'form': form})

def register_medical(request,is_admin,is_customer, is_employee):
    msg = None
    
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
  
            user = form.save(commit=False)
            user.is_employee = is_employee
            user.is_customer = is_customer
            user.is_admin = is_admin
            user.save()
            msg = 'user created'
            return redirect('login_view')
            
        else:
            msg = 'form is not valid'
    else:
        form = SignUpForm()
    return render(request,'account/register.html', {'form': form, 'msg': msg})

def register_patient(request,is_admin,is_customer, is_employee):
    msg = None
    
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            existing_patient = get_object_or_none(Patient, email=email)
            if existing_patient:
                messages.success(request,'registration successful')
                user = form.save(commit=False)
                user.is_employee = is_employee
                user.is_customer = is_customer
                user.is_admin = is_admin
                user.save()
                msg = 'user created'
                return redirect('login_view')

            else:
                messages.success(request,'Wait till your doctor add your informations')
                form=SignUpForm()

            
        else:
            msg = 'form is not valid'
    else:
        form = SignUpForm()
    return render(request,'account/register.html', {'form': form, 'msg': msg})


def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_admin:
                login(request, user)
                return redirect('adminpage')
            elif user is not None and user.is_customer:
                login(request, user)
                return redirect('customer')
            elif user is not None and user.is_employee:
                login(request, user)
                return redirect('employee')
            else:
                msg= 'invalid credentials'
        else:
            msg = 'error validating form'
    return render(request, 'account/login.html', {'form': form, 'msg': msg})


def admin(request):
    return render(request,'account/admin.html')


def customer(request):
    return render(request,'account/customer.html')


def employee(request):
    return render(request,'account/employee.html')




def get_object_or_none(model, email=None):
    filter_condition = Q()
    if email is not None:
        filter_condition |= Q(email=email)

    try:
        return model.objects.get(filter_condition)
    except model.DoesNotExist:
        return None
