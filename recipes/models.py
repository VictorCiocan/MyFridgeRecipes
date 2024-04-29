from django.db import models

# Create your models here.
quantity_type = (('1', 'pcs'),
                 ('2', 'grams'),
                 ('3', 'ml'))

difficulty_type = (('1', 'Easy'),
                   ('2', 'Medium'),
                   ('3', 'Experienced'))


class Ingredient(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    # type_quantity = models.CharField(max_length=20, choices=quantity_type, null=False, blank=False)

    # def get_type_quantity_display(self):
    #     return dict(quantity_type)[self.type_quantity]

    def __str__(self):
        return self.name


class RecipeModel(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    image = models.ImageField(upload_to='recipes/', null=True, blank=False)
    time = models.IntegerField(null=True, blank=False)
    difficulty = models.CharField(max_length=20, choices=difficulty_type, null=True, blank=False)
    ingredients = models.ManyToManyField(Ingredient, related_name="ingredients")

    def get_difficulty_display(self):
        return dict(difficulty_type)[self.difficulty]


    def get_recipe_steps(self):
        return self.recipesteps_set.all()

    def __str__(self):
        return f"{self.name} - id: {self.id} - {self.difficulty}"


#
# class IngredientsRecipe(models.Model):
#     ingredients = models.ForeignKey(IngredientsList, on_delete=models.CASCADE)
#     recipe = models.ForeignKey(RecipeModel, on_delete=models.CASCADE)
#     quantity = models.IntegerField(null=False, blank=False)
#     def __str__(self):
#         return f"{self.ingredients} - {self.quantity} - {self.ingredients.get_type_quantity_display()} - {self.recipe.name}"

class RecipeSteps(models.Model):
    recipe = models.ForeignKey(RecipeModel, on_delete=models.CASCADE)
    step_description = models.TextField(null=False, blank=False)

    def __str__(self):
        return f"Step for {self.recipe}"
