from django.db import models
from django.contrib.auth.models import User


TYPE_CHOICES = [('Bug', 'Bug'),
                ('Dark', 'Dark'),
                ('Dragon', 'Dragon'),
                ('Electric', 'Electric'),
                ('Flying', 'Flying'),
                ('Fairy', 'Fairy'),
                ('Fire', 'Fire'),
                ('Fighting', 'Fighting'),
                ('Ghost', 'Ghost'),
                ('Ground', 'Ground'),
                ('Grass', 'Grass'),
                ('Ice', 'Ice'),
                ('Normal', 'Normal'),
                ('Poison', 'Poison'),
                ('Psychic', 'Psychic'),
                ('Rock', 'Rock'),
                ('Steel', 'Steel'),
                ('Water', 'Water')
                ]


class Pokemon(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    type_1 = models.CharField(max_length=100, choices=TYPE_CHOICES)
    type_2 = models.CharField(max_length=100, choices=TYPE_CHOICES, null=True, blank=True)
    height = models.FloatField(null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)
    found = models.DateTimeField(auto_now_add=True)
    is_favorite = models.BooleanField(default=False)
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        ordering = ['-is_favorite']

    def __str__(self) -> str:
        return f'{self.name} - {self.species}'
