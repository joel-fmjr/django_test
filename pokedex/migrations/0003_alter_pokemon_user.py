# Generated by Django 4.0.6 on 2022-07-19 22:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pokedex', '0002_alter_pokemon_type_1_alter_pokemon_type_2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]