# Generated by Django 4.0.6 on 2022-07-19 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokedex', '0005_alter_pokemon_options_alter_pokemon_types'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pokemon',
            options={'ordering': ['-is_favorite']},
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='types',
            field=models.CharField(choices=[('BG', 'Bug'), ('DR', 'Dark'), ('DR', 'Dragon'), ('EL', 'Electric'), ('FL', 'Flying'), ('FR', 'Fairy'), ('FR', 'Fire'), ('FT', 'Fighting'), ('GH', 'Ghost'), ('GN', 'Ground'), ('GR', 'Grass'), ('IC', 'Ice'), ('NM', 'Normal'), ('PS', 'Poison'), ('PY', 'Psychic'), ('RC', 'Rock'), ('ST', 'Steel'), ('WT', 'Water')], max_length=100),
        ),
    ]
