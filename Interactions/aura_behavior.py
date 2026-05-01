"""
Auteur : Luc Desforges
Date : 1 mai 2026
Description :  Comportement de l'aura des NPCs du jeu, 
               qui inflige des dégâts au joueur s'il 
               se trouve à proximité d'un NPC.
"""
from Actors.npc_database import listof_dbnpc as npc_db
from Actors.player import player_instance as p_i

def detection_check(id: int):
    """
    But: Vérifie si le joueur est dans l'aura d'un NPC et 
    lui inflige des dégâts si c'est le cas.

    Entrée: id (int) - l'identifiant du NPC à vérifier.
    """
    npc_col = npc_db[id].get_col()
    npc_row = npc_db[id].get_row()
    player_col = p_i.get_col()
    player_row = p_i.get_row()
    aura = npc_db[id].aura
    """
    1 2 3 
    4 @ 5
    6 7 8
    """
    if(npc_col + aura == player_col 
       and (npc_row == player_row or            #4
            npc_row + aura == player_row or     #6
            npc_row - aura == player_row) or    #1                     
       npc_col - aura == player_col
       and (npc_row == player_row or            #5
            npc_row + aura == player_row or     #8
            npc_row - aura == player_row) or    #3
       npc_col == player_col 
       and (npc_row + aura == player_row or     #7
            npc_row - aura == player_row)       #2
    ):
        p_i.lose_life(npc_db[id].damage)