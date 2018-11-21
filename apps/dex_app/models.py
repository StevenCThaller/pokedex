# from django.db import models

# # Create your models here.



# class Evolution_Chain(models.Model):
#     baby_trigger_item = models.ForeignKey(Items, related_name='for_baby')


# class Pokemon_Species(models.Model):
#     name = models.CharField(max_lenth=25)
#     base_happiness = models.IntegerField()
#     capture_rate = models.IntegerField()
#     egg_groups = models.ManyToManyField(Egg_Groups, related_name='species')
#     evolution_trigger = models.CharField(max_length=25)
#     evolution_method = models.CharField(max_length=25)

# class Entries(models.Model):
#     entry_num = models.IntegerField()
#     pokemon_species = models.ForeignKey(Pokemon_Species, related_name='entry')

# class Pokedex(models.Model):
#     name = models.CharField(max_length=25)
#     entries = models.ManyToManyField(Entries, related_name='pokedex')
#     versions = models.ForeignKey


# class Regions(models.Model):
#     name = models.CharField(max_length=25)
#     pokedexes = models.ManyToManyField(Pokedex, related_name='region')
#     versions = models.ForeignKey

# class Generations(models.Model):
#     gen = models.CharField(max_length=25)
#     main_region = models.ForeignKey(Regions, related_name='main_generation')
#     moves = models.ForeignKey
#     pokemon = models.ForeignKey
#     types = models.ForeignKey
#     versions = models.ForeignKey

# class Encounter_Condition_Values(models.Model): 
#     name = models.CharField(max_length=55)

# class Encounter_Condition(models.Model):
#     name = models.CharField(max_length=55)
#     value = models.ForeignKey(Encounter_Condition_Values, related_name='encounter_condition')

# class Encounter_Method(models.Model):
#     name = models.CharField(max_length=55)
#     desc = models.CharField(max_length=255)

# class Location_Areas(models.Model):
#     name = models.CharField(max_length=25)

# class Locations(models.Model):
#     name = models.CharField(max_length=55)
#     areas = models.ForeignKey(Location_Areas, related_name='location')
#     region = models.ManyToManyField(Regions, related_name='locations') 
#     generation = models.ForeignKey(Generations, related_name='locations')
