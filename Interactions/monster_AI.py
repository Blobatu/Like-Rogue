from Actors.player import player_instance as p_i
from Actors.npc_database import listof_dbnpc as npc_db
from Actors.npc_repository import listof_npc as listof_type
from . import actor_movement as a_m

# nom = placeholder 

def Yplayer_distance(id: int = -1):
    return npc_db[id].position[1] - p_i.position[1]


def Xplayer_distance(id: int = -1):
    return npc_db[id].position[0] - p_i.position[0]

# valeur par défaut pour les positions de monstre

def search_sprite_by_line(line: str):
        for item in listof_type.values():
            col_found = line.find(item.sprite)
            print(f"{item.sprite}")
            if col_found == -1:
                continue
            return col_found


def algorithm():
    col_wow = -1
    row_wow = -1
    row_count = -1
    for line in a_m.console_tile:
        print(f"{line}")
        row_count += 1

        col_wow = search_sprite_by_line(line)
        print(f"{col_wow}, {row_count}")

        if col_wow == -1:
            continue

        if col_wow != -1:
            row_wow = row_count

        for id in npc_db:
            print(f"npc {id}: {npc_db[id].position}")
            
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