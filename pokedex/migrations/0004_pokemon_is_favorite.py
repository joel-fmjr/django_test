# Generated by Django 4.0.6 on 2022-07-19 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokedex', '0003_rename_wight_pokemon_weight'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='is_favorite',
            field=models.BooleanField(default=False),
        ),
    ]
