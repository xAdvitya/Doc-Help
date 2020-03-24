from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth

def register(request):

    if(request.method == 'POST'):
        first_name = request.POST['firstname']
        username = request.POST['username']
        password = request.POST['pass']
        conf_password = request.POST['confpass']



        if password == conf_password:
            if User.objects.filter(username=username).exists():
                print("username taken")
            else:
                user = User.objects.create_user(username=username,password=password,first_name=first_name)
                user.save()
        else:
            print('password not matching')

        return redirect("/")

    else:
        return render(request,"register/register.html")


def home(request):
    return render(request,"register/home.html")