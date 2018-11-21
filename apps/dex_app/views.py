from django.shortcuts import render, redirect
from .models import *
import pokebase as pb

def dex_page(request, version, id):
    newdexstr=""
    dexstr = str(id)
    while len(newdexstr) < (3-len(dexstr)):
        newdexstr += "0"
    newdexstr = "/static/dex_app/imgs/"+newdexstr+dexstr+".png"
    
    pokemon = pb.pokemon(id)

    moves = pokemon.moves
    lvlmov = {}

    for move in moves:
        for vgd in move.version_group_details:
            if vgd['version_group']['name'] == version and vgd['move_learn_method']['name'] == 'level-up':
                lvlmov[vgd['level_learned_at']] = move.move 

    lvlmov = dict(sorted(lvlmov.items()))

    
    context = {
        'version': version,
        'pokemon': pokemon,
        'picnum': newdexstr,
        'lvlupmoves': lvlmov
    }
    return render(request, 'dex_app/dex_page.html', context)

def pokedex(request):
    pokedex = []
    for i in range(1,2,1):
        pokedex.append({'id': i,
            'name': pb.pokemon(i).name,
            'type': pb.pokemon(i).types})
    context={
        'pokedex': pokedex,
    }
    return render(request,'dex_app/pokedex.html', context)

def pokedexshow(request):
    return render(request, 'dex_app/pokedex_show.html')
