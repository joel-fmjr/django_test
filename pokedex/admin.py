from django.contrib import admin
from .models import *


# Register your models here.

class PokemonAdmin(admin.ModelAdmin):
    list_display = ('name', 'species', 'types', 'is_favorite')
    search_fields = ['name','species', 'types']
    readonly_fields=('captured','pokedex')

class PokedexAdmin(admin.ModelAdmin):
    readonly_fields=('user',)
    
admin.site.register(Pokemon, PokemonAdmin)
admin.site.register(Pokedex, PokedexAdmin)
