from django.db import models

# Create your models here.
class clients(models.Model):
    Firsname = models.CharField(max_length=100)
    Lastname = models.CharField(max_length=100)
    CustID = models.IntegerField(max_length=6)
    PhoneNo = models.IntegerField(max_length=10)