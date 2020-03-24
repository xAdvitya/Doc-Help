from django.shortcuts import render,redirect


def home(request):
    return render(request,"pages/home.html")

def patients(request):
    return render(request,"pages/patients.html")

def patientDetail(request):
    pass