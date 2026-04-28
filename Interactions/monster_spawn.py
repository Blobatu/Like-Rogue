from .player_interactions import console_tile, replace_at_position
from Actors import npc

from .random_npc import r_npc
#from Level import full_level as fl
global col
col = -1
global row
row = -1
#import 
monster_list: list[npc.NPC] = []

monster_spawn = "& "
def spawn_monster():
    global row
    global col
    row_count = -1
    for i in console_tile:
        row_count += 1
        #print("-r-")
        #print(i)
        col = i.find(monster_spawn) 
        #print("-c-")
        #print(col)
        #print(i[col])
        if col != -1:
            row = row_count
            break
    
    r_npc.position = (col, row)
    #print(r_npc.position)
    #clear_old_position(r_npc.position[0], r_npc.position[1])
    replace_at_position(r_npc.position[0], r_npc.position[1], r_npc.sprite)
    monster_list.append(r_npc)  