from django.contrib import admin
from .models import *


class PokemonAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        if obj.species==Pokemon_specie.objects.get(name='Squirtle') and obj.level>15:
            obj.species = Pokemon_specie.objects.get(name='Wartotle')
        if obj.species==Pokemon_specie.objects.get(name='Wartotle') and obj.level>32:
            obj.species = Pokemon_specie.objects.get(name='Blastoise')

        super(PokemonAdmin, self).save_model(request, obj, form, change)


admin.site.register(Pokemon_specie)
admin.site.register(Pokemon_type)
admin.site.register(Pokemon, PokemonAdmin)

