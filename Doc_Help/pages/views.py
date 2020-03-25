from django.shortcuts import render,redirect
from .forms import PatientForm
from .models import Patient

def home(request):
    return render(request,"pages/home.html")

def patients(request):
    
    obj = Patient.objects.filter(user=request.user)
    names = []

    for i in obj:
        names.append(i.first_name)


    return render(request,"pages/patients.html",context={'names':names})

def patientDetail(request):

    form = PatientForm(request.POST or None,request.FILES or None)
    
    if form.is_valid():

        fs= form.save(commit=False)
        fs.user= request.user
        fs.save()

        form = PatientForm()

    context = {'form':form}
    
    return render(request,"pages/patientdet.html",context)
