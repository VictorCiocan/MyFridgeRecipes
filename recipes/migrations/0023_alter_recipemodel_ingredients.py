# Generated by Django 5.0.2 on 2024-03-27 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0022_delete_ingredients'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipemodel',
            name='ingredients',
            field=models.ManyToManyField(related_name='ingredients', to='recipes.ingredient'),
        ),
    ]
