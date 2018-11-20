import pokebase as pb



abilities = []

# Abilities
######################WORKS######################
i=1
while i < 233:
    ab = pb.ability(i)
    name = ab.name.replace('-', ' ')
    effect = ab.effect_entries[0].short_effect
    generation = ab.generation.id
    ability = [name.title(), effect, generation]
    print(ability)
    abilities.append(ability)
    i+=1