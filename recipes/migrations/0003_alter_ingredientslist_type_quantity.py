# Generated by Django 5.0.2 on 2024-03-06 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_ingredientslist_ingredientsrecipe_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredientslist',
            name='type_quantity',
            field=models.CharField(choices=[('1', 'pcs'), ('2', 'grams'), ('3', 'ml')], max_length=20),
        ),
    ]
