import sys
import os
from Interactions import player_interactions as p_i
from Interactions import monster_spawn
from Interactions import monster_AI
SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

print('\n'.join(p_i.console_tile))
monster_spawn.spawn_monster()
p_i.run()
while(True):
    print('\n'.join(p_i.console_tile))
    p_i.run()
    monster_AI.algorithm()
    #print("\033[H\033[J", end="")