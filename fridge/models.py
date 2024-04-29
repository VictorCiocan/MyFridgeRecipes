from django.db import models

from recipes.models import Ingredient
from django.contrib.auth.models import User

# Create your models here.



class FridgeIngredient(models.Model):

    id_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f" {self.ingredient.name} - {self.id_user}"
