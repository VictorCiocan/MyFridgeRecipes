# Generated by Django 5.0.2 on 2024-03-06 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0004_remove_ingredientsrecipe_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredientslist',
            name='type_quantity',
            field=models.CharField(choices=[('pcs', 'pcs'), ('grams', 'grams'), ('ml', 'ml')], max_length=20),
        ),
    ]
