"""
Auteur : Luc Desforges
Date : 1 mai 2026
Description :   Point d'entrée du jeu, qui initialise le donjon, 
                le joueur et les monstres,
"""
import sys
import os

import pygame
from Actors.npc_database import listof_dbnpc as npc_db
from Actors.player import player_instance as p_i
from Interactions import actor_movement as a_m
from Interactions import player_events as p_e
from Interactions import monster_spawn
from Interactions import monster_AI
from Interactions import dungeon

SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

p_i.set_position(6, dungeon.get_middle_row())
monster_spawn.spawn_monster()

def stats():
    return f"""
            Level: {p_i.level}
            XP: {p_i.progression.xp}/{p_i.progression.xp_to_next}
            Health: {p_i.health}/{p_i.max_health}   
            Potions: {p_i.potion_count}  
            Bombs: {p_i.bomb_count}
            """
def print_UI():
    print("\033[H\033[J", end="") 
    print(stats())
    print('\n'.join(dungeon.levels[p_i.level-1]))

pygame.mixer.init()
is_pressed = True
while(True):
    if p_i.is_alive():
        if is_pressed is True:    
            print_UI()
        is_pressed = p_e.listen_to_keyboard(is_pressed)
        if is_pressed is True:
            monster_AI.react_to_player_movement()
    else:
        for key, npc in npc_db.items():
            if npc is not None:
                if npc.sprite == '  ':
                    col, row = npc.position
                    a_m.replace_at_position(col, row, 'A ')
        print_UI()
        print(f"{p_i.name} is dead")
        break
    

