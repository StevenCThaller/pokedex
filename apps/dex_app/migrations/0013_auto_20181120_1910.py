# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-11-21 03:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dex_app', '0012_generations_dex_to'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entries',
            name='pokemon',
        ),
        migrations.RemoveField(
            model_name='pokedex',
            name='entries',
        ),
        migrations.RemoveField(
            model_name='generations',
            name='versions',
        ),
        migrations.DeleteModel(
            name='Entries',
        ),
        migrations.DeleteModel(
            name='Pokedex',
        ),
    ]
