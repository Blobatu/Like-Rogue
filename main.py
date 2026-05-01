"""
Auteur : Luc Desforges
Date : 14 avril 2026
Description : TODO
"""
import sys
import os
from Interactions.dungeon import dungeon_rows as dungeon
from Interactions import actor_movement as a_m
from Interactions import player_movement as p_m
from Interactions import monster_spawn
from Interactions import monster_AI

from Props import props_interaction as pr_i
SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

def columns_legend():
    legend: list[str] = []
    for i in range(dungeon[0].__len__()):
        index = str(i)[-1]
        if(index == '0'):
            index = '-'
        legend.append(index)
    return legend

a_m.p_i.set_position(6, 24)
monster_spawn.spawn_monster()
while(True):
    if a_m.p_i.is_alive():
        print("\033[H\033[J", end="")
        print("".join(columns_legend()))
        print('\n'.join(dungeon))
        p_m.listen_to_keyboard()
        monster_AI.algorithm()
    else:
        print(f"{a_m.p_i.name} is dead")
        break
    