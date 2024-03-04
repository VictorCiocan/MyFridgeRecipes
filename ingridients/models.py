from django.db import models

# Create your models here.

class IngredientModel(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.CharField(max_length=200, null=False, blank=False)
    quantity = models.CharField(max_length=50, null=False, blank=False)
    expiration_date = models.DateField(null=False, blank=False)