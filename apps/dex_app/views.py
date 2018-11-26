from django.shortcuts import render, redirect
from .models import *
import pokebase as pb




# Create your views here.
def dex_page(request, gen, id):
    newdexstr=""
    dexstr = str(id)
    while len(newdexstr) < (3-len(dexstr)):
        newdexstr += "0"
    newdexstr = "/static/dex_app/imgs/"+newdexstr+dexstr+".png"
    why = Generations.objects.get(gen=gen)
    pokemon = Pokemon.objects.get(id=id)

    versions = Versions.objects.filter(gen=why)

    movesingen = Pokemon_Learns_Move_By_Method.objects.filter(pokemon=pokemon)
    
    moveslist = []
    for version in versions:
        moveslist.append(movesingen.filter(version=version).order_by('meth_qual'))
    print(Learn_Methods.objects.all().values())
    context = {
        'gen': gen,
        'versions': versions,
        'pokemon': pokemon,
        'picnum': newdexstr,
        'moveslist': moveslist
    }
    return render(request, 'dex_app/pokedexshow.html', context)

def pokedex(request, gen):
    dex_to = Generations.objects.get(gen=gen)
    dex_to = dex_to.dex_to
    
    print(gen)
    if dex_to < 802:
        context = {
            'all_pokemon': Pokemon.objects.all()[0:dex_to],
            'gen': gen
        }
    else:
        context = {
            'all_pokemon': Pokemon.objects.all(),
            'gen': gen
        }
    
    return render(request,'dex_app/pokedex.html', context)

def moveshow(request, move, gen):
    monwholearn=[]
    mv = Moves.objects.get(name=move)
    movinmeth = Pokemon_Learns_Move_By_Method.objects.filter(move=Moves.objects.get(name=move.lower()))
    for version in Versions.objects.filter(gen=Generations.objects.get(gen=gen)):
        for mov in movinmeth:
            if mov.version.name == version.name:
                monwholearn.append(mov.pokemon)
    context = {
        'move': mv,
        'all_pokemon': monwholearn,
        'gen': gen
    }
    return render(request, 'dex_app/moveshow.html', context)

def moves(request, gen):
    
    context = {
        'all_moves': Moves.objects.all(),
        'gen': gen
    }

    return render(request, 'dex_app/moves.html', context)

def types(request):

    context = {
        'all_types': Types.objects.all(),
        'damage_rels': Damage_Relationships.objects.all()
    }

    return render(request, 'dex_app/types.html', context)

def showtypes(request, type):
    t = type

    context = {
        'type': Types.objects.get(tipe=t),
        'all_types': Types.objects.all(),
        'damage_rels': Damage_Relationships.objects.get(tipe=Types.objects.get(tipe=t))
    }

    return render(request, 'dex_app/typeshow.html', context)