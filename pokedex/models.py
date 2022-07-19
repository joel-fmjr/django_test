from django.db import models
from django.contrib.auth.models import User


TYPE_CHOICES = [('BG', 'Bug'),
                ('DR', 'Dark'),
                ('DR', 'Dragon'),
                ('EL', 'Electric'),
                ('FL', 'Flying'),
                ('FR', 'Fairy'),
                ('FR', 'Fire'),
                ('FT', 'Fighting'),
                ('GH', 'Ghost'),
                ('GN', 'Ground'),
                ('GR', 'Grass'),
                ('IC', 'Ice'),
                ('NM', 'Normal'),
                ('PS', 'Poison'),
                ('PY', 'Psychic'),
                ('RC', 'Rock'),
                ('ST', 'Steel'),
                ('WT', 'Water')
                ]


class Pokedex(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self) -> str:
        return f"{self.user.username}'s pokedex"


class Pokemon(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    types = models.CharField(max_length=100, choices=TYPE_CHOICES)
    height = models.FloatField(null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)
    captured = models.DateTimeField(auto_now_add=True)
    is_favorite = models.BooleanField(default=False)
    pokedex = models.ForeignKey(
        Pokedex, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        ordering = ['-is_favorite']

    def __str__(self) -> str:
        return f'{self.name} - {self.species}'
