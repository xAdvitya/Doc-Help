"""Doc_Help URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from register.views import register,login,logout
from pages.views import home,patients,patientAdd,removeObj
urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',register,name="register"),
    path('patients/',patients,name="patients"),
    path('patientadd/',patientAdd,name="patientadd"),
    path('login/',login,name="login"),
    path("remove/<int:pk>/",removeObj,name="remove"),
    path('register/logout/',logout,name="logout"),
    path('',home),
]