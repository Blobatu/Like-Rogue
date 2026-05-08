
"""
Auteur : Léonard  & Luc Desforges
Date : 1 mai 2026
Description : Module pour la gestion de l'apparition des monstres dans le jeu.
"""
import random

from Actors.player import player_instance as p_i
from Actors.npc import NPC
from . import actor_movement as a_m
from Actors import npc_database as npc_db
from . import dungeon
from .dungeon import damage_sprite
from .dungeon import monster_spawn
from Actors.npc_types import listof_npc as l


def spawn_monster():
    """
    But:    Fait apparaître des monstres sur la carte à 
            des positions aléatoires générées précedemment ("& ").
    """
    col = -1
    row = -1
    id = 0
    for line in dungeon.levels[p_i.level-1]:
        # On parcourt le donjon ligne par ligne pour 
        # trouver les positions de spawn des monstres
        row += 1
        col = line.find(monster_spawn)
        cols = [i for i, val in enumerate(line)if val+' ' == monster_spawn]
        for col in cols:
            if col != -1:
                # On trouve un spawn de monstre, 
                # on choisit un type de monstre aléatoire
                test = random.randint(1, 16)
                r_npc = None
                match test:
                    case 1:
                        r_npc = l["Goblin"]
                    case 3:
                        r_npc = l["Assassin"]
                    case 5:
                        r_npc = l["Orc"]
                    case 7:
                        r_npc = l["AuraFarmer"]
                if r_npc is None:
                    r_npc = l["Goblin"]

                # On crée une instance du monstre choisi et 
                # on la place de la position du spawn
                npc_db.listof_dbnpc[id] = NPC(name = r_npc.name,
                                            sprite = r_npc.sprite,
                                            health = r_npc.health,
                                            damage = r_npc.damage,
                                            aura = r_npc.aura,)
                npc_db.listof_dbnpc[id].set_position(col, row)
                a_m.replace_around_position(col, row, r_npc.aura, damage_sprite)
                a_m.replace_at_position(col, 
                                        row, 
                                        r_npc.sprite)
                
                # On ajoute le monstre à la base de données des NPCs
                id += 1
