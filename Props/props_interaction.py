import random as r
from Actors import player as p
from Actors import npc_database as npc_db
from Interactions import dungeon
from Interactions import actor_movement as am
from Level.level_generation import full_level as fl
from Interactions import monster_spawn
from Interactions import aura_behavior
"""
author : emmanuel Bissonnette
Goal : ce fichier contien les fonctions dinteraction avec les props 

"""
bomb_list: list[list] = []

def chest():
        """
        Description: Une fonction qui utilise un fichier pour recuperer une liste
            d'item a donner au joueur elle choisi aleatoirement et donne soit deux potions 
            ou deux bombes
        entrees:
        sorties:
        """
        item = r.randint(0,3)
        path = "Props/chest_item_list"
        file = open(path)
        lines = file.readlines()
        item = lines[item]
        item.strip()
        file.close()
        """
        if item != "health_pot":
           current_weapon = p.player_instance.weapon
           awnser = input(f"Vous avez trouve {item} voulez vous remplacer votre {current_weapon} Y ou N")
           if awnser == "Y" :
                p.player_instance.weapon = item
           elif awnser == "N":
                p.player_instance.weapon = current_weapon
            """
        if item == "health_pot":
            p.player_instance.potion_count += 2
        elif item == "bomb":
             p.player_instance.bomb_count += 2
def door ():
    """
    Description: cette fonction augmente le niveau au quel se trouve le joueur et
        genere un nouveau niveau elle teleporte le joueur au debut de celui ci et
        fait apparaitre les monstres
    entrees:
    sorties:
    """
    p.player_instance.level +=1 
    dungeon.dungeon_rows = fl()
    p.player_instance.position(6,24)
    monster_spawn.spawn_monster()


def spike_trap():
    """
    Description:une fonction qui retire une quantite aleatoire de vie aux joueur
    entrees:
    sorties:
    """
    p.player_instance.lose_life(r.randint(1,3))
def void ():
    """
    Description: une fonction qui retire la totalite de la vie du joueur
    entrees:
    sorties:
    """
    remaining_life = p.player_instance.health
    p.player_instance.lose_life(remaining_life)
        
def interaction_check(player_pos:str):
    """
    Description: cette fonction verifie si le joueur est sur un prop
        si oui il appelle la fonction lie a se prop
    entrees: la position du joueur en str
    sorties:
    """
    match player_pos:
        case "▤ ":
            chest()
        case "| ":
            door()
        case "△ ":
            spike_trap()
        case "":
            void()     
def bomb_interaction():
    """
    Description: cette fonction initialise une bombe avec ses coordonees 
         aisin que ces coordonees(celles du joueur) et  l'ajoute a une liste de bombe
    entrees:
    sorties:
    """
    #Verifie si le joueur a assez de bombe
    if p.player_instance.bomb_count > 0:
        p.player_instance.bomb_count -= 1
        bomb_position = p.player_instance.position
        #ajoute la bombe a la liste de bombe tout en initialisant le compteur
        bomb_info = [bomb_position,0]
        bomb_list.append(bomb_info)
        
        
def is_actor_on_bomb():
     """
    Description: cette fonction verifie que aucun acteur est sur la bombe avant
            de mettre le sprite de la bombe pour eviter de supprimer des acteurs
    entrees:
    sorties:
    """
     for bombs in bomb_list:
        if bombs[0] != p.player_instance.position:
             am.replace_at_position(bombs[0][0],bombs[0][1],dungeon.barrel_sprite)
        for key,npc in npc_db.listof_dbnpc.items():
             if npc is not None:
                if bombs[0]  != npc.position:
                    am.replace_at_position(bombs[0][0],bombs[0][1],dungeon.barrel_sprite)
def bomb_explodes():
    """
    Description: cette fonction attend que le conteur de la bombe soit a 5
                si oui la bombe explose la fonction verifie si un joueur ou un monstre se
                trouve a l'interieur de la range si oui elle cause du dommage la bombe 
                en explosant detruit les choses autour de elle en remplacent tout par de l'air
    entrees:
    sorties:
    """
    counter = 0
    for bombs in bomb_list:
        if bombs[1] > 5:
            if ((-5 <= bombs[0][1] - p.player_instance.get_row() <= 5 and 
                 -5*2 <= p.player_instance.get_col() <= 5*2)):
                p.player_instance.lose_life(r.randint(1,3))
            col, row = bombs[0]
            aura_behavior.aura_damage(False, col, row, 5, r.randint(1,5))
            bomb_list.pop(counter)
            am.replace_around_position(bombs[0][0],bombs[0][1],3,dungeon.air_sprite)
            am.replace_at_position(bombs[0][0],bombs[0][1],dungeon.air_sprite)
        counter += 1


def bomb_counter():
     """
    Description: ajoute aux compteur de chaque bombe pour donner un delai
    entrees:
    sorties:
    """
     for bombs in bomb_list:
          bombs[1] += 1
    
    

