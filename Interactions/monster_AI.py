"""
Auteur : Léonard  & Luc Desforges
Date : 1 mai 2026
Description : Module pour la gestion de l'IA des monstres du jeu, 
qui les fait se déplacer vers le joueur s'ils sont à proximité.
"""
from . import actor_movement as a_m
from Actors.player import player_instance as p_i
from Actors.npc_database import listof_dbnpc as npc_db


def Yplayer_distance(id: int = -1):
    """
    But:    Calcul la distance verticale entre le joueur et 
            un NPC donné par son id.
    Entrée: id (int) - l'identifiant du NPC à vérifier.
    Sortie: int - la distance verticale entre le joueur et le NPC.
    """
    return npc_db[id].get_row() - p_i.get_row()


def Xplayer_distance(id: int = -1):
    """
    But:    Calcul la distance horizontale entre le joueur et 
            un NPC donné par son id.
    Entrée: id (int) - l'identifiant du NPC à vérifier.
    Sortie: int - la distance horizontale entre le joueur et le NPC.
    """
    return npc_db[id].get_col() - p_i.get_col()


def react_to_player_movement():
    """
    But:    Algorithme de déplacement des NPCs du jeu, 
            qui les fait se déplacer vers le joueur s'ils sont à proximité.
    """
    for id in npc_db:
        if(npc_db[id] is None):
              continue 
        #print(str(id) + " : " + str(npc_db[id].position))
        npc_row = npc_db[id].get_row()
        min_row = npc_row - 6
        max_row = npc_row + 6
        npc_col = npc_db[id].get_col()
        min_col = npc_col - 12
        max_col = npc_col + 12

        if min_row <= p_i.get_row() <= max_row:
            # Le joueur est dans la zone verticale du NPC
            if(min_col <= p_i.get_col() <= max_col):
                # Le joueur est dans la zone horizontale du NPC

                if 0 > Yplayer_distance(id) > -3:
                        # Le joueur est en dessous du NPC, 
                        # le NPC se déplace vers le bas
                        a_m.move_down(id)

                elif 0 < Yplayer_distance(id) < 3:
                        # Le joueur est au dessus du NPC,
                        # le NPC se déplace vers le haut
                        a_m.move_up(id)
                        
                if 0 > Xplayer_distance(id) > -6:
                        # Le joueur est à droite du NPC,
                        # le NPC se déplace vers la droite
                        a_m.move_right(id)
                        
                elif 0 < Xplayer_distance(id) < 6:
                        # Le joueur est à gauche du NPC,
                        # le NPC se déplace vers la gauche
                        a_m.move_left(id)

                #print(Xplayer_distance(id))
                #print(Yplayer_distance(id))
                if (((npc_db[id].aura * -1) <= Yplayer_distance(id) <= npc_db[id].aura and 
                     (npc_db[id].aura * -1)*2 <= Xplayer_distance(id) <= npc_db[id].aura*2)):
                        p_i.lose_life(npc_db[id].damage)
                        