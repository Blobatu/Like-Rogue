import sys
import os
from Interactions import player_interactions as p_i
SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))


while(True):
    print('\n'.join(p_i.console_tile))
    p_i.run()
    print("\033[H\033[J", end="")