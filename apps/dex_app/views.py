from django.shortcuts import render, redirect
from .models import *
import pokebase as pb




# Create your views here.
def versionselect(request):
    vers = []
    for i in range(1, 17, 1):
        ver = pb.version_group(i)
        vers.append(ver)
    
    context = {
        'versions': vers
    }

    return render(request, 'dex_app/versionselect.html', context)

def dex_page(request, gen, id):
    newdexstr=""
    dexstr = str(id)
    while len(newdexstr) < (3-len(dexstr)):
        newdexstr += "0"
    newdexstr = "/static/dex_app/imgs/"+newdexstr+dexstr+".png"
    version = Generations.objects.get(gen=gen).versions.all()
    pokemon = Pokemon.objects.get(id=id)

    moves = Pokemon_Learns_Move_By_Method.objects.filter(pokemon=pokemon)
    
    

    
    context = {
        'gen': gen,
        'version': version,
        'pokemon': pokemon,
        'picnum': newdexstr,
    }
    print(context['pokemon'].types)
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

def moveshow(request):
    return render(request, 'dex_app/moveshow.html')

def moves(request):
    return render(request, 'dex_app/moves.html')