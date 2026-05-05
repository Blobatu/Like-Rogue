"""
Auteur : Luc Desforges
Date : 1 mai 2026
Description :  Comportement de l'aura des NPCs du jeu, 
               qui inflige des dégâts au joueur s'il 
               se trouve à proximité d'un NPC.
"""
from Actors.npc_database import listof_dbnpc as npc_db
from Actors.player import player_instance as p_i
from . import actor_movement as a_m
from .dungeon import exit_opened_sprite, air_sprite

def handle_dead_npc(key: int):
     npc = npc_db[key]
     if npc.health == 0:
          a_m.move_around_position(npc.get_col(), npc.get_row(), 
                                   npc.aura, air_sprite)
          a_m.clear_old_position(npc.get_col(), npc.get_row())
          p_i.listof_npc_killed[p_i.npc_killed_count] = npc_db[key]
          if p_i.progression.gain_xp(True) is True:
               a_m.replace_at_position(222, 24, exit_opened_sprite)
          npc_db[key] = None

def aura_damage(is_player: bool, 
                col: int = 0, row: int = 0, aura: int = 0, damage: int = 0):
    """
    But: Vérifie si un acteur est dans la zone de dégat et 
    lui inflige des dégâts si c'est le cas.

    Entrée:    is_player (bool) - si la source de dégat est le joueur.
               col (int) - la colonne de la source de dégat
               row (int) - la rangée de la source de dégat
               aura (int) - la taille de la zone de dégat
               damage (int) - le nombre de dégat de la zone
    """
    if(is_player is True):
        detection_check_player(-1)
    else:
        for key, obj in npc_db.items():
          if obj is None:
               continue
          for i in range(col-aura * 2, col+aura * 2 + 2):
               for j in range(row-aura, row + aura + 1):
                    if obj.position == (i, j):
                         if npc_db[key].lose_life(damage) is True:
                              handle_dead_npc(key)


def detection_check_player(npc_id: int):
     """
     But: Vérifie si le joueur est dans l'aura d'un NPC et 
     lui inflige des dégâts si c'est le cas.

     Entrée: id (int) - l'identifiant du NPC à vérifier.
     """
     if npc_id == -1:
          detection_check(p_i.get_col(), p_i.get_row(), 2, p_i.damage)
     else:
          col = npc_db[npc_id].get_col()
          row = npc_db[npc_id].get_row()
          target_col = p_i.get_col()
          target_row = p_i.get_row()
          aura = npc_db[npc_id].aura

          if check_surrounding(col, row, 
                               target_col, target_row, aura) is True:
               p_i.lose_life(npc_db[npc_id].damage)
     return -1


def detection_check(position: tuple[int, int], aura: int, damage: int):
     return detection_check(position[0], position[1])


def detection_check(col: int, row: int, aura: int, damage: int):
     """
     But: Vérifie si le joueur est dans l'aura d'un event et 
     lui inflige des dégâts si c'est le cas.

     Entrée: 
               col (int) - la colonne de la source de dégat
               row (int) - la rangée de la source de dégat
               aura (int) - la taille de la zone de dégat
               damage (int) - le nombre de dégat de la zone
     """
     for key, obj in npc_db.items():
          if obj is None:
               continue
          for i in range(col-aura*2, col+aura*2+2):
               for j in range(row-aura, row+aura+1):
                    if obj.position == (i, j):
                         if npc_db[key].lose_life(damage) is True:
                              handle_dead_npc(key)

     return -1



def check_surrounding(col: int, row: int, 
                      target_col: int, target_row: int, aura: int):
    """
    1 2 3 
    4 @ 5
    6 7 8
    """
    if(col + aura == target_col 
       and (row == target_row or            #4
            row + aura == target_row or     #6
            row - aura == target_row) or    #1                     
       col - aura == target_col
       and (row == target_row or            #5
            row + aura == target_row or     #8
            row - aura == target_row) or    #3
       col == target_col 
       and (row + aura == target_row or     #7
            row - aura == target_row)       #2
    ):
        return True
    return False