from django.contrib import admin
from .models import *


# Register your models here.

class PokemonAdmin(admin.ModelAdmin):
    list_display = ('name', 'species', 'types')
    
    @admin.display(description='Tamanho do nome')
    def teste(self, obj):
        return len(obj.name)

    #teste.short_description = "Tamanho do nome"


admin.site.register(Pokemon, PokemonAdmin)
admin.site.register(Pokedex)
