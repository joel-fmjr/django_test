# Generated by Django 4.0.6 on 2022-07-19 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokedex', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='type_1',
            field=models.CharField(choices=[('Bug', 'Bug'), ('Dark', 'Dark'), ('Dragon', 'Dragon'), ('Electric', 'Electric'), ('Flying', 'Flying'), ('Fairy', 'Fairy'), ('Fire', 'Fire'), ('Fighting', 'Fighting'), ('Ghost', 'Ghost'), ('Ground', 'Ground'), ('Grass', 'Grass'), ('Ice', 'Ice'), ('Normal', 'Normal'), ('Poison', 'Poison'), ('Psychic', 'Psychic'), ('Rock', 'Rock'), ('Steel', 'Steel'), ('Water', 'Water')], max_length=100),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='type_2',
            field=models.CharField(blank=True, choices=[('Bug', 'Bug'), ('Dark', 'Dark'), ('Dragon', 'Dragon'), ('Electric', 'Electric'), ('Flying', 'Flying'), ('Fairy', 'Fairy'), ('Fire', 'Fire'), ('Fighting', 'Fighting'), ('Ghost', 'Ghost'), ('Ground', 'Ground'), ('Grass', 'Grass'), ('Ice', 'Ice'), ('Normal', 'Normal'), ('Poison', 'Poison'), ('Psychic', 'Psychic'), ('Rock', 'Rock'), ('Steel', 'Steel'), ('Water', 'Water')], max_length=100, null=True),
        ),
    ]
