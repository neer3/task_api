from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime
from django.contrib.auth.models import User


# Create your models here.


class Task_List(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(default=" ", max_length=50)
    startDate = models.DateField(auto_now=False, auto_now_add=False)
    endDate = models.DateField(auto_now=False, auto_now_add=False)
    remarks = models.CharField(default=" ", max_length=100)
