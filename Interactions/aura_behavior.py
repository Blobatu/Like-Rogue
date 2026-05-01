"""
Auteur : Luc Desforges
Date : 14 avril 2026
Description : TODO
"""
from Actors.npc_database import listof_dbnpc as npc_db
from Actors import player as p

def detection_check(id: int):
    npc_col = npc_db[id].get_col()
    npc_row = npc_db[id].get_row()
    player_col = p.player_instance.get_col()
    player_row = p.player_instance.get_row()
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
        print("Combat !")
        print("player position : " + str(p.player_instance.position))
        print("monster position : " + str(npc_db[id].position))