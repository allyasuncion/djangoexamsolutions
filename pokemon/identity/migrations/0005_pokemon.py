# Generated by Django 3.2.3 on 2021-05-25 04:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('identity', '0004_pokemon_specie_pokemon_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=200, null=True)),
                ('level', models.FloatField(null=True)),
                ('species', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='identity.pokemon_specie')),
            ],
        ),
    ]
