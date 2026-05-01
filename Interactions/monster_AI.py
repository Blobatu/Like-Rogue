from Actors.player import player_instance as p_i
from Actors.npc_database import listof_dbnpc as npc_db
from Actors.npc_repository import listof_npc as listof_type
from . import actor_movement as a_m

# nom = placeholder 

def Yplayer_distance(id: int = -1):
    return npc_db[id].get_row() - p_i.get_row()


def Xplayer_distance(id: int = -1):
    return npc_db[id].get_col() - p_i.get_col() * 2

# valeur par défaut pour les positions de monstre

def search_sprite_by_line(line: str):
        for item in listof_type.values():
            col_found = line.find(item.sprite)
            #print(f"{item.sprite}")
            if col_found == -1:
                continue
            return col_found

def check_limit(i:int):
    if(i > 48):
        return a_m.console_tile[48].find(p_i.sprite)

    if(i < 0):
        return a_m.console_tile[0].find(p_i.sprite)
    
    return a_m.console_tile[i].find(p_i.sprite)

def algorithm():

    for id in npc_db:
        print(f"npc {id}: {npc_db[id].position}")
        npc_row = npc_db[id].get_row()
        min_row = npc_row - 3
        max_row = npc_row + 3
        npc_col = npc_db[id].get_col()
        min_col = npc_col - 5
        max_col = npc_col + 5

        if min_row <= p_i.get_row() <= max_row:
            if(min_col <= p_i.get_col()*2 <= max_col):
                if Yplayer_distance(id) < 2:
                    if npc_db[id].get_row() + 1 != p_i.get_row():
                        a_m.move_down(id)
                        
                elif Yplayer_distance(id) > -2:
                    if npc_db[id].get_row() - 1 != p_i.get_row():
                        a_m.move_up(id)
                        
                if Xplayer_distance(id) < 2:
                    if npc_db[id].get_col() + 1 != p_i.get_col()*2:
                        a_m.move_right(id)
                        
                elif Xplayer_distance(id) > -2:
                    if npc_db[id].get_col() - 1 != p_i.get_col():
                        a_m.move_left(id)
                        