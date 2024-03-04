from django.db import models

# Create your models here.

class RecipeModel(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    ingredients = models.CharField(max_length=100, null=False, blank=False)
    time_minutes = models.CharField(max_length=100, null=False, blank=False)