from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm, UserTypeForm, PatientSignUpForm
from django.contrib.auth import authenticate, login, logout
from doctor.models import Patient
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.db.models import Q
import qrcode
from io import BytesIO
import base64
import pyotp
from .models import GoogleAuthenticator
from .decorators import redirect_home, login_required_customized


# Create your views here.
@redirect_home
def login_register(request):
    return render(request, "login_register.html")


@login_required_customized
def logout_user(request):
    logout(request)
    return redirect("login_view")


@redirect_home
def user_type(request):
    if request.method == "POST":
        form = UserTypeForm(request.POST)
        if form.is_valid():
            is_radiologist = form.cleaned_data["is_radiologist"]
            is_doctor = form.cleaned_data["is_doctor"]
            is_patient = form.cleaned_data["is_patient"]
            if is_radiologist or is_doctor:
                return redirect(
                    "register_medical",
                    is_radiologist=is_radiologist,
                    is_doctor=is_doctor,
                    is_patient=is_patient,
                )
            elif is_patient:
                return redirect(
                    "register_patient",
                    is_radiologist=is_radiologist,
                    is_doctor=is_doctor,
                    is_patient=is_patient,
                )
        else:
            messages.error(request, "Please select only one role")
    else:
        form = UserTypeForm()
    return render(request, "account/user_type.html", {"form": form})


@redirect_home
def register_medical(request, is_radiologist, is_doctor, is_patient):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_patient = is_patient
            user.is_doctor = is_doctor
            user.is_radiologist = is_radiologist
            user.save()

            # Generate a random secret key for the user
            secret_key = pyotp.random_base32()

            # Create a new GoogleAuthenticator object for the user
            ga = GoogleAuthenticator.objects.create(user=user, secret_key=secret_key)

            # Generate the QR code image
            otp_uri = ga.get_otp_uri()
            img = qrcode.make(otp_uri)
            buffer = BytesIO()
            img.save(buffer, format="PNG")
            qr_image = base64.b64encode(buffer.getvalue()).decode()

            # Add success message
            messages.success(request, "User created successfully")

            # Render the registration template with the QR code image and other data
            return render(request, "account/qr.html", {"qr_image": qr_image})
        else:
            # Add error message
            messages.error(request, "Form is not valid")
    else:
        form = SignUpForm()

    return render(request, "account/register.html", {"form": form})


@redirect_home
def register_patient(request, is_radiologist, is_doctor, is_patient):
    if request.method == "POST":
        form = PatientSignUpForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            cin_number = form.cleaned_data["cin_number"]

            existing_patient = get_object_or_none(
                Patient, email=email, cin_number=cin_number
            )
            print(existing_patient)
            if existing_patient:
                user = form.save(commit=False)
                user.is_patient = is_patient
                user.is_doctor = is_doctor
                user.is_radiologist = is_radiologist
                user.save()
                messages.success(request, "User created")
                # Generate a random secret key for the user
                secret_key = pyotp.random_base32()
                # Create a new GoogleAuthenticator object for the user
                ga = GoogleAuthenticator.objects.create(
                    user=user, secret_key=secret_key
                )
                # Generate the QR code image
                otp_uri = ga.get_otp_uri()
                img = qrcode.make(otp_uri)
                buffer = BytesIO()
                img.save(buffer, format="PNG")
                qr_image = base64.b64encode(buffer.getvalue()).decode()
                # Render the registration template with the QR code image and other data
                return render(request, "account/qr.html", {"qr_image": qr_image})

            else:
                messages.info(request, "Wait till your doctor adds your information")
                form = PatientSignUpForm()

        else:
            messages.error(request, "Form is not valid")
    else:
        form = PatientSignUpForm()

    return render(request, "account/patientregister.html", {"form": form})


@redirect_home
def login_view(request):
    form = LoginForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            otp = request.POST["otp"]

            user = authenticate(username=username, password=password)
            try:
                ga = GoogleAuthenticator.objects.get(user=user)
            except GoogleAuthenticator.DoesNotExist:
                ga = None

            if ga is not None:
                totp = pyotp.TOTP(ga.secret_key)
                if totp.verify(otp):
                    if user is not None and user.is_radiologist:
                        login(request, user)
                        messages.success(
                            request, "You have successfully logged in as a radiologist."
                        )
                        return redirect("radiologist")
                    elif user is not None and user.is_doctor:
                        login(request, user)
                        messages.success(
                            request, "You have successfully logged in as a doctor."
                        )
                        return redirect("doctor")
                    elif user is not None and user.is_patient:
                        login(request, user)
                        messages.success(
                            request, "You have successfully logged in as a patient."
                        )
                        return redirect("patient_appointments")
                else:
                    messages.error(request, "Invalid OTP")
            else:
                messages.error(request, "Invalid credentials")
        else:
            messages.error(request, "Error validating form")
    return render(request, "account/login.html", {"form": form})


def get_object_or_none(model, email=None, cin_number=None, **kwargs):
    filter_condition = Q()
    if email is not None:
        filter_condition &= Q(email=email)
    if cin_number is not None:
        filter_condition &= Q(cin_number=cin_number)
    if kwargs:
        filter_condition &= Q(**kwargs)

    try:
        return model.objects.get(filter_condition)
    except model.DoesNotExist:
        return None
