from django.contrib import admin
from .models import *


# Register your models here.

class PokemonAdmin(admin.ModelAdmin):
    list_display = ('name', 'species', 'type_1', 'type_2', 'is_favorite')
    search_fields = ('name','species', 'type_1', 'type_2')
    readonly_fields=('found','user')

    
admin.site.register(Pokemon, PokemonAdmin)
