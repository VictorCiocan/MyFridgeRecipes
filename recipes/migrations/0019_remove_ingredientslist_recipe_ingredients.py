# Generated by Django 5.0.2 on 2024-03-27 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0018_ingredientslist_recipe_delete_ingredientsrecipe'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingredientslist',
            name='recipe',
        ),
        migrations.CreateModel(
            name='Ingredients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('type_quantity', models.CharField(choices=[('1', 'pcs'), ('2', 'grams'), ('3', 'ml')], max_length=20)),
                ('recipe', models.ManyToManyField(to='recipes.recipemodel')),
            ],
        ),
    ]