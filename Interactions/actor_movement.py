"""
Auteur : Léonard  & Luc Desforges
Date : 1 mai 2026
Description : Module pour la gestion des déplacements des acteurs dans le jeu.
"""
from Interactions.aura_behavior import detection_check
from Props.props_interaction import interaction_check
from Actors.npc_database import listof_dbnpc as npc_db
from Actors.player import player_instance as p_i
from .dungeon import dungeon_rows as dungeon
from .dungeon import whitelist_sprites
from .dungeon import player_sprite
from .dungeon import wall_sprite
from .dungeon import air_sprite


def move_up(id: int = -1):
    """
    But: Permet de déplacer le npc vers le haut

    Entrées: 
        id: L'identifiant du NPC à déplacer, -1 pour le joueur
    """
    move(is_vertical=True, 
         is_negative=True,
         id=id)


def move_down(id: int = -1):
    """
    But: Permet de déplacer le npc vers le bas

    Entrées:
        id: L'identifiant du NPC à déplacer, -1 pour le joueur
    """
    move(is_vertical=True, 
         is_negative=False,
         id=id)


def move_left(id: int = -1):
    """
    But: Permet de déplacer le npc vers la gauche

    Entrées:
        id: L'identifiant du NPC à déplacer, -1 pour le joueur
    """
    move(is_vertical=False, 
         is_negative=True,
         id=id)


def move_right(id: int = -1 ):
    """
    But: Permet de déplacer le npc vers la droite

    Entrées:
        id: L'identifiant du NPC à déplacer, -1 pour le joueur
    """
    move(is_vertical=False, 
         is_negative=False,
         id=id)


def move(is_vertical: bool, is_negative: bool, id: int = -1):
    """
    But: Permet de déplacer le npc

    Entrées: 
        is_vertical: Verifie si le mouvement est vertical,
        is_negative: Vrai si le mouvement va vers le haut ou la gauche
    """
    if(id == -1):
        col, row = p_i.position
    else:
        col, row = npc_db[id].position

    new_col, new_row = col, row

    if(is_vertical is True):
        # Le mouvement est vertical, on modifie la rangée
        new_row = new_position_value(row, is_negative)
    else:
        # Le mouvement est horizontal, on modifie la colonne
        new_col = new_position_value(col, is_negative, step=2)

    if is_wall(new_col, new_row):
        # Si le joueur va vers un mur,
        # on ne bouge pas et on affiche un message
        message_wall()
        return

    # Si le mouvement est valide, on efface l'ancienne position de l'acteur
    clear_old_position(col, row)
    

    if(id == -1):
        # Si c'est le joueur qui se déplace, 
        # on met à jour sa position
        replace_at_position(new_col, new_row, player_sprite)
        p_i.set_position(new_col, new_row)
    else:
        # Si c'est un NPC qui se déplace,
        # on met à jour sa position
        replace_at_position(new_col, new_row, npc_db[id].sprite)
        npc_db[id].set_position(new_col, new_row)
        
        # Après le déplacement du NPC, 
        # on vérifie si le joueur est dans son aura
        detection_check(id)


def new_position_value(original_value: int, is_negative: bool, step: int = 1):
    """
    But: Permet de calculer la nouvelle valeur de 
    la colonne ou de la rangée après un déplacement.

    Entrées:
        original_value: La valeur originale de la colonne ou de la rangée,
        is_negative: Vrai si le mouvement va vers le haut ou la gauche,
        step: Le nombre de cases à déplacer 
        (1 pour les mouvements verticaux, 2 pour les mouvements horizontaux)
    Sortie: La valeur de la colonne ou de la rangée après le déplacement
    """
    if(is_negative is True):
        return original_value - step
    else:
        return original_value + step


def is_wall(col, row):
    """
    But: Permet de verifier si le joueur va vers un mur

    Entrées: 
        col: La colonne à vérifier,
        row: La rangée à vérifier,
    Sortie: Vrai si le joueur va vers un mur, sinon Faux
    """
    if(col < 0 or col >= len(dungeon[0])):
        return True
    if(row < 0 or row >= len(dungeon)):
        return True
    if(dungeon[row][col: col+2] == wall_sprite):
        return True
    
    sprite = dungeon[row][col]
    interaction_check(sprite+" ")
    
    if sprite+" " not in whitelist_sprites:
        return True
    
    return False


def message_wall():
    print("You can't move there")


def clear_old_position(col: int, row: int):
    """
    But:    Permet d'effacer l'ancienne position de 
            l'acteur en la remplaçant par un sprite d'air
    Entrées:
        col: La colonne de l'ancienne position,
        row: La rangée de l'ancienne position,
    """
    replace_at_position(col, row, air_sprite)

def replace_at_position(col: int, row: int, value: str):
    """
    But:    Permet de remplacer le sprite à une position donnée
    Entrées:
        col: La colonne de la position à remplacer,
        row: La rangée de la position à remplacer,
        value: Le sprite à placer à la position donnée
    """
    before_value = dungeon[row][:col]
    after_value = dungeon[row][col+2:]
    insert_at_position(row, before_value, after_value, value)


def insert_at_position(row: int, 
                       before_value: str, 
                       after_value: str, 
                       value: str):
    """
    But:    Permet d'insérer un sprite à une position donnée
    Entrées:
        row: La rangée de la position à remplacer,
        before_value: La partie de la ligne avant la position à remplacer,
        after_value: La partie de la ligne après la position à remplacer,
        value: Le sprite à placer à la position donnée
    """
    dungeon[row] = before_value + value + after_value