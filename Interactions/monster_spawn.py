
from Actors import npc
from Actors import npc_database as npc_db
from Actors.npc_repository import listof_npc as l
from . import actor_movement as a_m
import random

global col
col = -1
global row
row = -1

monster_list: list[npc.NPC] = []

monster_spawn = "&"
def spawn_monster():
    global row
    global col
    row_count = -1
    print('\n'.join(a_m.console_tile))

    for i in a_m.console_tile:
        row_count += 1
        col = i.find(monster_spawn)

        #print(f"{col}, {row_count}")
        
        if col != -1:
            row = row_count
            r_npc = random.choice(list(l.values()))
            print(r_npc.sprite)
            r_npc.set_position(col, row)
            a_m.replace_at_position(r_npc.get_col(), 
                                    r_npc.get_row(), 
                                    r_npc.sprite)
            npc_db.add_npc_to_db(r_npc)
            #print(f"npc: {r_npc.position}")