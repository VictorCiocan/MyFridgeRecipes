from lib2to3.fixes.fix_input import context

from django.db.models import Count
from django.shortcuts import render
from django.template.context_processors import request
from django.views.generic.edit import CreateView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin

from fridge.models import FridgeIngredient
from recipes.models import RecipeModel


# Create your views here.


class FridgeListView(LoginRequiredMixin, ListView):
    template_name = 'fridge/myingredient_list.html'
    model = FridgeIngredient


    context_object_name = 'ingredient'

    # def get_queryset(self):
    #     # Retrieve the ingredients in the customer's fridge
    #     user_fridge_ingredients = FridgeIngredient.objects.filter(id_user=self.request.user).values_list('ingredient',
    #                                                                                                      flat=True)
    #
    #     # Filter recipes that contain any of the ingredients in the fridge
    #     queryset = RecipeModel.objects.filter(ingredients__in=user_fridge_ingredients).annotate(
    #         num_ingredients=Count('ingredients')).order_by('-num_ingredients').distinct()

    # return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ingredient'] = context['ingredient'].filter(id_user_id=self.request.user)
        ingredients = FridgeIngredient.objects.filter(id_user=self.request.user).values_list('ingredient_id')
        recipes = RecipeModel.objects.filter(ingredients__in=ingredients).distinct()
        context['recipes'] = recipes
        # context['filtered_recipes'] = self.get_queryset()
        return context


# def fridgeingredients(request):
#     context = {}
#     fridgeingredients = FridgeIngredient.objects.all()
#
#     context['fridgeingredients'] = fridgeingredients
#
#
#     return render(request, 'fridge/fridgeingredients.html', context)


class FridgeCreateView(LoginRequiredMixin, CreateView):
    model = FridgeIngredient
    template_name = 'fridge/fridge_form.html'
    fields = ['ingredient']
    success_url = reverse_lazy('myfridge_list')

    def form_valid(self, form):
        form.instance.id_user = self.request.user
        return super(FridgeCreateView, self).form_valid(form)


class DeleteView(LoginRequiredMixin, DeleteView):
    model = FridgeIngredient
    context_object_name = 'fridgeingredients'
    success_url = reverse_lazy('myfridge_list')

    # def get(self, *args, **kwargs):
    #     return self.post(*args, **kwargs)
