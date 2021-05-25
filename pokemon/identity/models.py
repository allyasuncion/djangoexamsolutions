from django.db import models
from django.contrib.auth.models import User


class Pokemon_type(models.Model):
    name = models.CharField(max_length=200, null=True)

    class Meta:
        verbose_name = ('Pokemon type')

    def __str__(self):
        return self.name


class Pokemon_specie(models.Model):
    name = models.CharField(max_length=200, null=True)
    evolution_level = models.FloatField(null=True)
    next_evolution = models.ForeignKey('self', blank=True, null=True, on_delete=models.SET_NULL)
    pokemon_type = models.ManyToManyField('Pokemon_type', blank=True)

    class Meta:
        verbose_name = ('Pokemon specie')

    def __str__(self):
        return self.name


class Pokemon(models.Model):
    nickname = models.CharField(max_length=200, null=True)
    species = models.ForeignKey('Pokemon_specie', blank=True, null=True, on_delete=models.SET_NULL)
    level = models.FloatField(null=True)
    trainer = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = ('Pokemon')


    def __str__(self):
        return self.nickname




