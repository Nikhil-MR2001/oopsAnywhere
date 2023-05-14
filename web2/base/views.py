from django.contrib import messages, auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect

from .forms import NewUserForm
from .models import farm


# Create your views here.
def index(request):
    obj = farm.objects.all()
    return render(request, 'index.html', {'obj': obj})


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration Successfully")
            return redirect("register")
        messages.error(request, "Unsuccessful registration")

    form = NewUserForm
    return render(request, 'register.html', {"register_form": form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"you are login from {username}")
                return redirect("/")
            else:
                messages.error(request, "enter a valid password or username ")
        else:
            messages.error(request, "enter a valid password or username ")

    form = AuthenticationForm()
    return render(request, 'login.html', {'login_form': form})


def logout_request(request):
    auth.logout(request)
    return redirect('/')
