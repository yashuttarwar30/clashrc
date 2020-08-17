from django.db import models

from django.contrib.auth.models import User

class Userprofile(models.Model):
    first_name = models.CharField(max_length=10, blank=False)
    last_name = models.CharField(max_length=10, blank=False)
    email = models.CharField(max_length=10, blank=False)
    phno=models.CharField(max_length=10,blank=False)
    gender=models.CharField(max_length=10,blank=False)
    def __str__(self):
        return self.first_name + " "+self.last_name
