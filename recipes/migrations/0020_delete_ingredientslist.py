# Generated by Django 5.0.2 on 2024-03-27 18:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fridge', '0002_alter_fridgeingredients_id_ingredients_list'),
        ('recipes', '0019_remove_ingredientslist_recipe_ingredients'),
    ]

    operations = [
        migrations.DeleteModel(
            name='IngredientsList',
        ),
    ]