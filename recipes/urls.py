from django.contrib import admin
from django.urls import path, include

from recipes.views import RecipesListView, RecipeDetailView, recipe_detail

urlpatterns = [
    path('', RecipesListView.as_view(), name='recipes-all'),
    path('detail/<int:pk>', recipe_detail, name='recipes-detail'),

]
