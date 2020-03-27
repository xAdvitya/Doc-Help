from django.shortcuts import render,redirect,get_object_or_404
from .forms import PatientForm
from .models import Patient

def home(request):
    return render(request,"pages/home.html")

def patients(request):
    
    if request.user.is_authenticated:
            
        obj = Patient.objects.filter(user=request.user.pk)


        return render(request,"pages/patients.html",context={'names': obj})

    else:
        return render(request,"register/login.html")

def patientAdd(request):

    if request.user.is_authenticated:
       
        form = PatientForm(request.POST or None,request.FILES or None)
        
        if form.is_valid():

            fs= form.save(commit=False)
            fs.user= request.user
            fs.save()

            form = PatientForm()

        context = {'form':form}
        
        return render(request,"pages/patientadd.html",context)

    else:
        return render(request,"register/login.html")


def removeObj(request,pk):

    object = Patient.objects.get(pk=pk)
    object.delete()
    return redirect("/patients/")