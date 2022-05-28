
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render
from .models import *
from django.utils import timezone
from django.contrib.auth.decorators import login_required


def index(request):
    main_doctors = MainDoctor.objects.all()
    context = {
        'main_doctors':main_doctors
    }
    return render(request,
                  template_name='index.html', context=context)


def doctors(request):
    doctors = AttendingDoctor.objects.all()
    context = {
        'doctors':doctors
    }
    return render(request,
                  template_name='doctors.html', context=context)


def hospitals(request):
    hospitals = Hospital.objects.all()
    context = {
        'hospitals':hospitals
    }
    return render(request,
                  template_name='hospitals.html', context=context)

def nurses(request):
    nurses = Nurse.objects.all()
    context = {
        'nurses':nurses
    }
    return render(request,
                  template_name='nurses.html', context=context)

def patients(request):
    patients = Patient.objects.all()
    context = {
        'patients':patients
    }
    return render(request,
                  template_name='patients.html', context=context)

def signupuser(request):
    if request.method == 'GET':
        return render(request, 'signupuser.html', {'form':UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST[
                    'password1'])
                user.save()
                login(request, user)
                return redirect('account')
            except IntegrityError:
                return render(request, 'signupuser.html', {'form':UserCreationForm(), 'error':'Это имя пользователя уже занято. Пожалуйста, выберите новое имя пользователя'})
        else:
            return render(request, 'signupuser.html', {'form':UserCreationForm(), 'error':'Пароли не совпадают'})


def loginuser(request):
    if request.method == 'GET':
        return render(request, 'loginuser.html', {'form':AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'loginuser.html', {'form':AuthenticationForm(), 'error':'Логин и пароль не совпадают'})
        else:
            login(request, user)
            return redirect('account')

@login_required
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')

def account(request):
    return render(request, template_name='account.html')