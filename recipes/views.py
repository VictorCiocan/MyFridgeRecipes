from django.db.models import Count
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from fridge.models import FridgeIngredient
from recipes.models import *


# Create your views here.

class RecipesListView(ListView):
    template_name = "recipes/recipes_all.html"
    model = RecipeModel



class RecipeDetailView(DetailView):
    template_name = "recipes/recipe_detail.html"
    model = RecipeModel

    # def get_context_data(self, **kwargs):
    #     context = super(RecipeDetailView, self).get_context_data(**kwargs)
    #     context["stepslist"] = [{"step_description": "Step 1"}, {"step_description": "Step 2"}]
    #     return context


def recipe_detail(request, pk):
    context = {}
    recipe = RecipeModel.objects.filter(id=pk).all()
    steps = RecipeSteps.objects.filter(recipe_id=pk)
    ingredients = RecipeModel.objects.filter(id=recipe[0].id).values("ingredients__name")

    context['recipe'] = recipe
    context['steps'] = steps
    context['ingredients'] = ingredients

    #RecipeModel.objects.filter(ingredients__in=[1,2,3])
    return render(request, 'recipes/recipe_detail.html', context)


class RecipeStepsListView(ListView):
    template_name = "recipes/recipe_detail.html"
    model = RecipeSteps

    def get_context_data(self, **kwargs):
        context = super(RecipeStepsListView, self).get_context_data(**kwargs)
        context["stepslist"] = [{"step_description": "Step 1"}, {"step_description": "Step 2"}]
        return context


def index(request):
    recipes = RecipeModel.objects.all()
    steps = RecipeStepsListView.as_view()

    return render(request, "recipes/recipes_all.html", {"recipes": recipes, "steps": steps})
