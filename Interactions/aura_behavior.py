"""
Auteur : Luc Desforges
Date : 1 mai 2026
Description :  Comportement de l'aura des NPCs du jeu, 
               qui inflige des dégâts au joueur s'il 
               se trouve à proximité d'un NPC.
"""
from Actors.npc_database import listof_dbnpc as npc_db
from Actors.player import player_instance as p_i

def detection_check(npc_id: int):
     """
     But: Vérifie si le joueur est dans l'aura d'un NPC et 
     lui inflige des dégâts si c'est le cas.

     Entrée: id (int) - l'identifiant du NPC à vérifier.
     """
     if npc_id == -1:
          aura = 3
          col, row = p_i.position

          for key, obj in npc_db.items():
               if obj is None:
                    continue
               print(f"test {obj.position}")
               for i in range(col-aura*2, col+aura*2+2):
                    for j in range(row-aura, row+aura+1):
                         if obj.position == (i, j):
                                   if npc_db[key].lose_life(p_i.damage) is True:
                                        return key
     else:
          col = npc_db[npc_id].get_col()
          row = npc_db[npc_id].get_row()
          target_col = p_i.get_col()
          target_row = p_i.get_row()
          aura = npc_db[npc_id].aura

          if check_surrounding(col, row, target_col, target_row, aura) is True:
               p_i.lose_life(npc_db[npc_id].damage)
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