import sys
import os
from Interactions import player_interactions as p_i
from Interactions import monster_spawn
from Interactions import monster_AI
SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

def columns_legend():
    legend: list[str] = []
    for i in range(p_i.console_tile[0].__len__()):
        index = str(i)[-1]
        if(index == '0'):
            index = '-'
        legend.append(index)
    return legend

monster_spawn.spawn_monster()
print(p_i.r_npc.position)
print(p_i.p.player_instance.position)
print("".join(columns_legend()))
print('\n'.join(p_i.console_tile))
p_i.run()
monster_AI.algorithm()
while(True):
    print("\033[H\033[J", end="")
    print(p_i.r_npc.position)
    print(p_i.p.player_instance.position)

    print("".join(columns_legend()))
    print('\n'.join(p_i.console_tile))
    p_i.run()
    monster_AI.algorithm()