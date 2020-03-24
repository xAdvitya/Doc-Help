from django.db import models

class Patient(models.Model):
    first_name = models.TextField(max_length=30)
    last_name = models.TextField(max_length=30)
    age = models.IntegerField()
    numvisit = models.IntegerField()
    detail = models.TextField(max_length=500)
