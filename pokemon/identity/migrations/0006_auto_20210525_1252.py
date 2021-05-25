# Generated by Django 3.2.3 on 2021-05-25 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('identity', '0005_pokemon'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pokemon_specie',
            name='pokemon_type',
        ),
        migrations.AddField(
            model_name='pokemon_specie',
            name='pokemon_type',
            field=models.ManyToManyField(blank=True, null=True, to='identity.Pokemon_type'),
        ),
    ]
