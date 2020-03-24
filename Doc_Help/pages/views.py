from django.shortcuts import render,redirect
from .forms import PatientForm

def home(request):
    return render(request,"pages/home.html")

def patients(request):
    return render(request,"pages/patients.html")

def patientDetail(request):

    form = PatientForm(request.POST or None)
    
    if form.is_valid():

        form.save()
        form = PatientForm()

    context = {'form':form}
    
    return render(request,"pages/patientdet.html",context)
