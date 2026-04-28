from .player_interactions import insert_at_position, console_tile
from Actors.npc_repository import listof_npc as l
import random
global npc
npc = random.l
col = -1
row = -1
#import 
monster_list = []

monster_spawn = [".&"]
def spawn_monster():
    for i in console_tile:
        col =i.find(monster_spawn) 
        if col != -1:
            row = i
            break

    npc.position = (col, row)
    insert_at_position(col,row,npc.sprite)

"""
if level is beginning:
    monster_list.clear()
    spawn_monster()
    for monster in console_tile:
        monster_list.append(l.name)
"""    