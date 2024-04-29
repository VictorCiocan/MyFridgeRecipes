from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=30, unique=True, null=False, blank=False )
    first_name = models.CharField(max_length=30, null=True, blank=False)
    last_name = models.CharField(max_length=30, null=True, blank=False)
    password = models.CharField(max_length=20, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    gender = models.CharField(max_length=1, null=False, blank=False)
    age = models.IntegerField(null=False, blank=False)

