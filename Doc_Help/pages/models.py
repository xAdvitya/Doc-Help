from django.db import models
from django.contrib.auth.models import User

class Patient(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    
    first_name = models.TextField(max_length=30)
    last_name = models.TextField(max_length=30)
    age = models.IntegerField()
    numvisit = models.IntegerField()
    detail = models.TextField(max_length=500)
