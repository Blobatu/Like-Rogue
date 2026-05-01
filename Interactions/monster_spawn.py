
"""
Auteur : Léonard  & Luc Desforges
Date : 1 mai 2026
Description : Module pour la gestion de l'apparition des monstres dans le jeu.
"""
import random
from . import actor_movement as a_m
from Actors import npc_database as npc_db
from .dungeon import dungeon_rows as dungeon
from Actors.npc_repository import listof_npc as l

monster_spawn = "& "

def spawn_monster():
    """
    But:    Fait apparaître des monstres sur la carte à 
            des positions aléatoires générées précedemment ("& ").
    """
    col = -1
    row = -1
    print('\n'.join(dungeon))

    for line in dungeon:
        # On parcourt le donjon ligne par ligne pour 
        # trouver les positions de spawn des monstres
        row += 1
        col = line.find(monster_spawn)
        
        if col != -1:
            # On trouve un spawn de monstre, 
            # on choisit un type de monstre aléatoire
            r_npc = random.choice(list(l.values()))

            # On crée une instance du monstre choisi et 
            # on la place de la position du spawn
            r_npc.set_position(col, row)
            a_m.replace_at_position(r_npc.get_col(), 
                                    r_npc.get_row(), 
                                    r_npc.sprite)
            
            # On ajoute le monstre à la base de données des NPCs
            npc_db.add_npc_to_db(r_npc)