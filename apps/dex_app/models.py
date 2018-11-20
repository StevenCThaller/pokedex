from django.db import models

# Create your models here.
class Abilities(models.Model):
    name = models.CharField(max_length=25)
    effect = models.CharField(max_length=255)

class Types(models.Model):
    tipe = models.CharField(max_length=15)

class Damage_Relationships(models.Model):
    type_ = models.ForeignKey(Types, related_name='damage_relationship')
    double_from = models.ManyToManyField(Types, related_name='double_to')
    double_to = models.ManyToManyField(Types, related_name='double_from')
    half_from = models.ManyToManyField(Types, related_name='half_to')
    half_to = models.ManyToManyField(Types, related_name='half_from')
    none_from = models.ManyToManyField(Types, related_name='none_to')
    none_to = models.ManyToManyField(Types, related_name='nome_from')

class Damage_Types(models.Model):
    name = models.CharField(max_length=25)

class Moves(models.Model):
    name = models.CharField(max_length=25)
    type_ = models.ForeignKey(Types, related_name='moves')
    category = models.ForeignKey(Damage_Types, related_name='moves')
    pp = models.IntegerField()
    power = models.IntegerField()
    accuracy = models.IntegerField()

class Pokemon(models.Model):
    name = models.CharField(max_length=30)
    types = models.ManyToManyField(Types, related_name='pokemon')
    abilities = models.ManyToManyField(Abilities, related_name='pokemon')
    bst = models.IntegerField()
    hp = models.IntegerField()
    attack = models.IntegerField()
    defense = models.IntegerField()
    sp_attack = models.IntegerField()
    sp_defense = models.IntegerField()
    speed = models.IntegerField()

class Learn_Methods(models.Model):
    method = models.CharField(max_length=25)

class Pokemon_Learns_Move_By_Method(models.Model):
    pokemon = models.ForeignKey(Pokemon, related_name='learns_move_by_method')
    move = models.ForeignKey(Moves, related_name='pokemon_learns_by_method')
    method = models.ForeignKey(Learn_Methods, related_name='pokemon_learns_move_by')
    meth_qual = models.CharField(max_length=10)

class Entries(models.Model):
    entry_num = models.IntegerField()
    pokemon = models.ForeignKey(Pokemon, related_name='entry')

class Pokedex(models.Model):
    name = models.CharField(max_length=25)
    entries = models.ManyToManyField(Entries, related_name='pokedex')

class Versions(models.Model):
    name = models.CharField(max_length=25)
    move_learn_methods = models.ManyToManyField(Learn_Methods, related_name='version')
    pokedexes = models.ManyToManyField(Pokedex, related_name='generation')

class Generations(models.Model):
    gen = models.CharField(max_length=25)
    abilities = models.ManyToManyField(Abilities, related_name='generation')
    moves = models.ManyToManyField(Moves, related_name='generation')
    pokemon = models.ManyToManyField(Pokemon, related_name='generation')
    types = models.ManyToManyField(Types, related_name='generation')
    versions = models.ForeignKey(Versions, related_name='generation')