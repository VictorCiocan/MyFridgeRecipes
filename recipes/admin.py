from django.contrib import admin

from recipes.models import RecipeModel, Ingredient, RecipeSteps

# Register your models here.
admin.site.register(RecipeModel)
admin.site.register(Ingredient)
admin.site.register(RecipeSteps)

