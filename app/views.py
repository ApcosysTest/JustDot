from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.contrib.auth import authenticate, logout, login
from django.contrib import messages

# Index page
def index(request):
    return render(request, 'index.html')

# Register page
def register(request):
    context = {}
    if request.POST:
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('RegisterConfirm')
        else:
            messages.error(request, "Please Correct Below Errors")
            context['registration_form'] = form
    else:
        form = RegisterForm()
        context['registration_form'] = form
    return render(request, "register.html", context)

# Login Page
def login_view(request):
    context = {}
    user = request.user
    if user.is_authenticated:
        return redirect("index")
    if request.method == "POST":
        form = LoginForm(request.POST, request.POST)
        if form.is_valid():
            email = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            print(email, password)
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
            else:
                print(user)
            return redirect("index")
    else:
        form = LoginForm()
    context['login_form'] = form
    return render(request, "login.html", context)

# Logout function
def logout_view(request):
    logout(request)
    return redirect("index")

# Create Resume Page
def createResume(request):
    return render(request, 'createResume.html')

# Register Confirmation page
def RegisterConfirm(request):
    return render(request, 'registerConfirmation.html')

# Forget Password page
def forgotPassword(request):
    return render(request, 'forgotPassword.html')

def resumeDetail(request):
    return render(request, 'resumeDetail.html')