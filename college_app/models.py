from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Login(AbstractUser):
    is_college = models.BooleanField(default=False)

class college(models.Model):
    name = models.CharField(max_length=20)
    place = models.CharField(max_length=20)
    contact_no = models.IntegerField()
    e_mail = models.CharField(max_length=20)



class student(models.Model):
    user = models.ForeignKey(Login, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    Roll_no = models.IntegerField()
    contact_no = models.IntegerField()
    e_mail = models.CharField(max_length=20)