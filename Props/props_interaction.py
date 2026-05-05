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
        Description: Une fonction qui utilise  une liste
            d'item a donner au joueur elle choisi aleatoirement et donne soit deux potions 
            ou une bombes
        entrees:
        sorties:
        """
        #liste contenu possible du coffre
        chest_content = ["bomb","potion","potion"]
        random_item = r.randint(0,2)
        # verifie si cest une bombe si oui bombe +1
        if chest_content[random_item] == "bomb":
            p.player_instance.bomb_count += 1
        #verifie si cest une potion si oui potion +2
        if chest_content[random_item] == "potion":
            p.player_instance.potion_count += 2
       
def door ():
    """
    Description: cette fonction augmente le niveau au quel se trouve le joueur et
        genere un nouveau niveau elle teleporte le joueur au debut de celui ci et
        fait apparaitre les monstres
    entrees:
    sorties:
    """
    #print("\033[H\033[J", end="")
    col, row = p.player_instance.position
    p.player_instance.level +=1 
    am.replace_at_position(col, row, dungeon.exit_closed_sprite)
    p.player_instance.set_position(6, 24)
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
        # pose la bombe au coordonee du joueur
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
        #cette ligne compare les coordonee du joueur avec celle de la bombe pour eviter de 
        # supprimer le joueur
        if bombs[0] != p.player_instance.position:
             am.replace_at_position(bombs[0][0], bombs[0][1],
                                    dungeon.barrel_sprite)
        # cette boucle verifie que aucun enemi dans la list de npc se trouve sur la bombe
        # pour eviter de le remplacer
        for key,npc in npc_db.listof_dbnpc.items():
             if npc is not None:
                if bombs[0]  != npc.position:
                    am.replace_at_position(bombs[0][0], bombs[0][1], 
                                           dungeon.barrel_sprite)
def bomb_explodes():
    """
    Description: cette fonction attend que le conteur de la bombe soit a 5
                si oui la bombe explose la fonction verifie si un joueur ou un monstre se
                trouve a l'interieur de la range si oui elle cause du dommage la bombe 
                en explosant detruit les choses autour de elle en remplacent tout par de l'air
    entrees:
    sorties:
    """
    #initialisation du compteur pour savoir quelle bombe pop
    counter = 0
    for bombs in bomb_list:
        if bombs[1] > 10:
            aura = 3
            damage = r.randint(1,3)
            #le if verifie que le joueur se situe bien dans la range de 5 de la bombe 
            # pour savoir si il faut lui faire des degats
            col, row = p.player_instance.position
            if ((-aura <= bombs[0][1] - row <= aura and 
                 -aura * 2 <= bombs[0][0] - col <= aura * 2)):
                p.player_instance.lose_life(damage)
            col, row = bombs[0]
            aura_behavior.aura_damage(False, col, row, 3, damage)
            bomb_list.pop(counter)
            # cette fonction fait le dommage autour de la bombe en remplacent les tiles autour
            am.replace_around_position(bombs[0][0], bombs[0][1], 
                                       aura, dungeon.air_sprite)
            am.replace_around_position(bombs[0][0], bombs[0][1],
                                       aura, dungeon.air_sprite,
                                       dungeon.wall_sprite)
             #celle ci retire la bombe elle meme 
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
