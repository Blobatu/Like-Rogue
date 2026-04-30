from Actors.player import player_instance as p_i
from Actors.npc_database import listof_dbnpc as npc_db
from Actors.npc_repository import listof_npc as l
from . import actor_movement as a_m
# nom = placeholder 

def Xplayer_distance(id: int = -1):
    return npc_db[id].position[1] - p_i.position[1]


def Yplayer_distance(id: int = -1):
    return npc_db[id].position[0] - p_i.position[0]

# valeur par défaut pour les positions de monstre

def algorithm():
    col_wow = -1
    row_wow = -1
    row_count = -1
    for i in a_m.console_tile:
        row_wow += 1

        for item in l.values():
            col_wow = i.find(item.sprite)
            break

        if col_wow == -1:
            continue

        if col_wow != -1:
            row_wow = row_count

        for id in npc_db:

            if -2 < Yplayer_distance(id) <2 and -4 < Xplayer_distance(id) < 0:
                if npc_db[id].position[1] + 1 != p_i.position[1]:
                    print("move down")
                    a_m.move_down(id)
                break
                #move down
    
            if -2 < Yplayer_distance(id) <2 and 0 < Xplayer_distance(id) < 4:
                if npc_db[id].position[1] - 1 != p_i.position[1] :
                    print("move up")
                    a_m.move_up(id)
                break
                #move up
    
            if -2 < Xplayer_distance(id) < 2 and -4 < Yplayer_distance(id) < 0:
                if npc_db[id].position[0] - 1 != p_i.position[0]:
                    print("move right")
                    a_m.move_right(id)
                break
                #move right
    
            if -2 < Xplayer_distance(id) < 2 and 0 < Yplayer_distance(id) < 4:
                if npc_db[id].position[1] + 1 != p_i.position[1]:
                    print("move left")
                    a_m.move_left(id)
                break
                #move_left