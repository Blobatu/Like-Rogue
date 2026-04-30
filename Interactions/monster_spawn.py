
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
    for i in a_m.console_tile:
        row_count += 1
        col = i.find(monster_spawn)
        if col != -1:
            row = row_count
            r_npc = random.choice(list(l.values()))
            r_npc.position = (int(col / 2), row)
            a_m.move_at_position(r_npc.position[0], 
                             r_npc.position[1], 
                             r_npc.sprite)
            npc_db.add_npc_to_db(r_npc)
  