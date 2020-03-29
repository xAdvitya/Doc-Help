from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth

def login(request):
    
    if (not request.user.is_authenticated):

        if(request.method == 'POST'):

            username = request.POST['username']
            password = request.POST['pass']

            user = auth.authenticate(username=username,password=password)

            if user is not None:
                auth.login(request,user)
                return redirect('patients')
            else:
                messages.info(request,'wrong username or password')
                return redirect('login')
        else:
            return render(request,"register/login.html")
    else:
        return redirect("/")

def logout(request):

    auth.logout(request)
    return redirect('login')

def register(request):

    if(request.method == 'POST'):

        first_name = request.POST['firstname']
        username = request.POST['username']
        password = request.POST['pass']
        conf_password = request.POST['confpass']


        if username != '':
            print(username)

            if (not len(password) < 8):
               
                if User.objects.filter(username=username).exists():
                    messages.info(request,"Enter * digit password")
                    return redirect("register")
                else:
                    user = User.objects.create_user(username=username,password=password,first_name=first_name)
                    user.save()
                    return redirect("login")
                    
            elif(password == conf_password):
                
                return redirect("login")

            else:
                messages.info(request,'password not matching')
                return redirect("register")
            
        else:
            return render(request,"register/register.html")

    else:
        return render(request,"register/register.html")
        


