from django.shortcuts import render
from django.views.generic import ListView

from ingridients.models import IngredientModel
from recipes.models import RecipeModel, Ingredient


# Create your views here.
class HomeView(ListView):
    template_name = 'home/home.html'
    model = RecipeModel

    def get_context_data(self, **kwargs):
        context= super(HomeView, self).get_context_data(**kwargs)
        context['ingredients'] = Ingredient.objects.all().count()
        context['recipies'] = RecipeModel.objects.all().count()
        return context

