import sys
import os
from Interactions import player_interactions as p_i
SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
p_i.run()