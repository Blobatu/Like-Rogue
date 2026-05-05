"""
Auteur : Luc Desforges
Date : 1 mai 2026
Description : Base de données pour les NPCs du jeu.
"""
from . import npc

dbnpc_id: int = 0

listof_dbnpc: dict[int, npc.NPC] = {
}

def add_npc_to_db(npc: npc.NPC):
    global dbnpc_id
    listof_dbnpc[dbnpc_id] = npc
    dbnpc_id += 1