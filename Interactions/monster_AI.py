"""
Auteur : Léonard  & Luc Desforges
Date : 14 avril 2026
Description : TODO
"""
from Actors.player import player_instance as p_i
from Actors.npc_database import listof_dbnpc as npc_db
from Actors.npc_repository import listof_npc as listof_type
from . import actor_movement as a_m


def Yplayer_distance(id: int = -1):
    return npc_db[id].get_row() - p_i.get_row()


def Xplayer_distance(id: int = -1):
    return npc_db[id].get_col() - p_i.get_col()


def search_sprite_by_line(line: str):
        for item in listof_type.values():
            col_found = line.find(item.sprite)

            if col_found == -1:
                continue
            
            return col_found


def check_limit(i: int):
    if(i > 48):
        return a_m.console_tile[48].find(p_i.sprite)
    if(i < 0):
        return a_m.console_tile[0].find(p_i.sprite)
    
    return a_m.console_tile[i].find(p_i.sprite)


def algorithm():
    for id in npc_db:
        npc_row = npc_db[id].get_row()
        min_row = npc_row - 6
        max_row = npc_row + 6
        npc_col = npc_db[id].get_col()
        min_col = npc_col - 12
        max_col = npc_col + 12

        if min_row <= p_i.get_row() <= max_row:
            if(min_col <= p_i.get_col() <= max_col):
                if 0 > Yplayer_distance(id) > -3:
                        a_m.move_down(id)
                        
                elif 0 < Yplayer_distance(id) < 3:
                        a_m.move_up(id)
                        
                if 0 > Xplayer_distance(id) > -6:
                        a_m.move_right(id)
                        
                elif 0 < Xplayer_distance(id) < 6:
                        a_m.move_left(id)