# Generated by Django 5.0.2 on 2024-03-06 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0008_alter_ingredientslist_type_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredientslist',
            name='type_quantity',
            field=models.CharField(choices=[('1', 'pcs'), ('2', 'grams'), ('3', 'ml')], max_length=20),
        ),
    ]
