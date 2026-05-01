from pandas import col

from Actors.player import player_instance as p_i
from Interactions.aura_behavior import detection_check
from Level.level_generation import full_level as fl
from Actors.npc_database import listof_dbnpc as npc_db
from Props.props_interaction import interaction_check

wall_sprite = "##"
player_sprite = "@ "
air_sprite = ". "
exit_sprite = "|"
barrel_sprite = "! "
chest_sprite = "▤ "
spike_trap_sprite = "△ "

whitelist_sprites = [air_sprite, chest_sprite, barrel_sprite, exit_sprite, spike_trap_sprite]

global console_tile
# vieile map utilisée pour les tests.
# console_tile = ["####################",
#                 "##. . . . . . . . ##",
#                 "##. . . . . . . . ##",
#                 "##. . . . @ . . . ##",
#                 "##. . . . . . . . ##",
#                 "####################"]

console_tile = fl()

console_tile = fl()

def move_up(id: int = -1):
    move(is_vertical=True, 
         is_negative=True,
         id=id)


def move_down(id: int = -1):
    move(is_vertical=True, 
         is_negative=False,
         id=id)


def move_left(id: int = -1):
    move(is_vertical=False, 
         is_negative=True,
         id=id)


def move_right(id: int = -1 ):
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
        new_row = new_position_value(row, is_negative)

    else:
        new_col = new_position_value(col, is_negative, step=2)

    if is_wall(new_col, new_row):
        message_wall()
        return

    clear_old_position(col, row)

    if(id == -1):
        set_new_position(new_col, new_row, player_sprite)
        p_i.set_position(new_col, new_row)

    else:
        set_new_position(new_col, new_row, npc_db[id].sprite)
        npc_db[id].set_position(new_col, new_row)

    # luc pourquoi tu as mis ça ?
    detection_check()


def new_position_value(original_value: int, is_negative: bool, step: int = 1):
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
    if(col < 0 or col >= len(console_tile[0])):
        return True
    if(row < 0 or row >= len(console_tile)):
        return True
    if(console_tile[row][col: col+2] == wall_sprite):
        return True
    
    sprite = console_tile[row][col]
    interaction_check(sprite+" ")
    
    if sprite+" " not in whitelist_sprites:
        return True
    
    return False


def message_wall():
    print("You can't move there")


def clear_old_position(col: int, row: int):
    replace_at_position(col, row, air_sprite)


def set_new_position(col: int, row: int, value: str):
    replace_at_position(col, row, value)


def replace_at_position(col: int, row: int, value: str):
    before_value = console_tile[row][:col]
    after_value = console_tile[row][col+2:]
    insert_at_position(row, before_value, after_value, value)


def insert_at_position(row: int, 
                       before_value: str, 
                       after_value: str, 
                       value: str):
    console_tile[row] = before_value + value + after_value