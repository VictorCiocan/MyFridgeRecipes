# Generated by Django 5.0.2 on 2024-03-06 18:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_alter_ingredientslist_type_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingredientsrecipe',
            name='name',
        ),
    ]
