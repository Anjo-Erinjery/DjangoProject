from django.db import models

# Create your models here.
class User(models.Model):
    username=models.CharField(max_length=50,unique=True) 
    password=models.CharField(max_length=50) 
    email=models.EmailField()


def _str_(self): 
    return self.username
