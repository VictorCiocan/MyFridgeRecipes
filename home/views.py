from django.shortcuts import render
from django.views.generic import ListView

from ingridients.models import IngredientModel


# Create your views here.
class HomeView(ListView):
    template_name = 'home/home.html'
    model = IngredientModel

