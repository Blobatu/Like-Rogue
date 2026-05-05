"""
Auteur : Luc Desforges
Date : 1 mai 2026
Description :   Point d'entrée du jeu, qui initialise le donjon, 
                le joueur et les monstres,
"""
import sys
import os
from Actors.player import player_instance as p_i
from Interactions import player_movement as p_m
from Interactions import monster_spawn
from Interactions import monster_AI
from Interactions import dungeon

SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

def columns_legend():
    legend: list[str] = []
    for i in range(dungeon.levels[p_i.level-1].__len__()):
        index = str(i)[-1]
        if(index == '0'):
            index = '-'
        legend.append(index)
    return legend

p_i.set_position(6, 24)
monster_spawn.spawn_monster()

while(True):
    if p_i.is_alive():
        #print("\033[H\033[J", end="")
        print("".join(columns_legend()))
        print(p_i.position)
        print(p_i.level)
        print('\n'.join(dungeon.levels[p_i.level-1]))
        p_m.listen_to_keyboard()
        monster_AI.react_to_player_movement()
    else:
        print(f"{p_i.name} is dead")
        break
    
