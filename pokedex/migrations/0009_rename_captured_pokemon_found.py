# Generated by Django 4.0.6 on 2022-07-19 21:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pokedex', '0008_remove_pokemon_id_remove_pokemon_pokedex_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pokemon',
            old_name='captured',
            new_name='found',
        ),
    ]