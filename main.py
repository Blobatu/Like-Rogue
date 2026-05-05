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

p_i.set_position(6, 24)
monster_spawn.spawn_monster()

is_pressed = True
while(True):
    if p_i.is_alive():
        if is_pressed is True:    
            print("\033[H\033[J", end="") 
            print(
f"""
    Level: {p_i.level}
    XP: {p_i.progression.xp}/{p_i.progression.xp_to_next}
    Health: {p_i.health}/{p_i.max_health}   
    Potions: {p_i.potion_count}  
    Bombs: {p_i.bomb_count}
 """)
            print('\n'.join(dungeon.levels[p_i.level-1]))
        is_pressed = p_m.listen_to_keyboard(is_pressed)
        monster_AI.react_to_player_movement()
    else:
        print(f"{p_i.name} is dead")
        break
    
