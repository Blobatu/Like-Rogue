import sys
import os
from Interactions import player_interactions as p_i
from Interactions import monster_spawn
from Interactions import monster_AI
from Interactions import actor_movement as a_m
from Props import props_interaction as pr_i
SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

def columns_legend():
    legend: list[str] = []
    for i in range(a_m.console_tile[0].__len__()):
        index = str(i)[-1]
        if(index == '0'):
            index = '-'
        legend.append(index)
    return legend

monster_spawn.spawn_monster()
while(True):
    #print("\033[H\033[J", end="")
    
    print("".join(columns_legend()))
    print('\n'.join(a_m.console_tile))
    p_i.run()
    monster_AI.algorithm()