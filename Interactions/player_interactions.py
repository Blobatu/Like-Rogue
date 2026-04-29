'''
Auteur: Léonard Lefebvre
Date: 14 avril
Description: to do
'''
from pandas import col

from Actors import player as p
from Level.level_generation import make_lvl_data, gen_maze
from .random_npc import r_npc
from Actors import npc
import keyboard as k
wall_sprite = "##"
player_sprite = "@ "
air_sprite = ". "
#player_position = player.position
mobs =("player","other_monsters")

global console_tile

console_tile = make_lvl_data(gen_maze())

global player_position
player_position = (5, 3)  # col 5, row 3
p.player_instance.position = player_position

# mouvement 
def move_up():
    move(is_vertical=True, 
         is_negative=True)


def move_down():
    move(is_vertical=True, 
         is_negative=False)


def move_left():
    move(is_vertical=False, 
         is_negative=True)


def move_right():
    move(is_vertical=False, 
         is_negative=False)


def move(is_vertical: bool, is_negative: bool):
    """
    But: Permet de déplacer le joueur

    Entrées: 
        is_vertical: Verifie si le mouvement est vertical,
        is_negative: Vrai si le mouvement va vers le haut ou la gauche
    """
    global console_tile, player_position
    col, row = p.player_instance.position
    new_col, new_row = col, row

    if(is_vertical is True):
        new_row = new_position_value(row, is_negative)

    else:
        new_col = new_position_value(col, is_negative)

    if is_wall(new_col, new_row):
        message_wall()
        return
        
    clear_old_position(col, row)
    set_new_position(new_col, new_row, player_sprite)
    p.player_instance.position = (new_col, new_row)
    player_position = p.player_instance.position
    if(r_npc.position[0] + 1 == p.player_instance.position[0] 
       and (r_npc.position[1] == p.player_instance.position[1] or
            r_npc.position[1] + 1 == p.player_instance.position[1] or
            r_npc.position[1] - 1 == p.player_instance.position[1]) or                         
       r_npc.position[0] - 1 == p.player_instance.position[0]
       and (r_npc.position[1] == p.player_instance.position[1] or
            r_npc.position[1] + 1 == p.player_instance.position[1] or
            r_npc.position[1] - 1 == p.player_instance.position[1]) or
       r_npc.position[0] == p.player_instance.position[0] 
       and (r_npc.position[1] + 1 == p.player_instance.position[1] or
            r_npc.position[1] - 1 == p.player_instance.position[1])
    ):
        print("Combat !")
        print("player position : " + str(p.player_instance.position))
        print("monster position : " + str(r_npc.position))


def new_position_value(original_value: int, is_negative: bool):
    if(is_negative is True):
        return original_value - 1
    
    else:
        return original_value + 1


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
    if(console_tile [row] [col * 2 : col * 2 + 2 ] == wall_sprite):
        return True
        
    return False


def message_wall():
    print("You can't move there")


def clear_old_position(col: int, row: int):
    move_at_position(col, row, air_sprite)


def set_new_position(col: int, row: int, value: str):
    move_at_position(col, row, value)


def move_at_position(col: int, row: int, value: str):
    before_value = console_tile[row][:col*2]
    after_value = console_tile[row][col*2+2:]
    insert_at_position(row, before_value, after_value, value)


def replace_at_position(col: int, row: int, value: str):
    before_value = console_tile[row][:col]
    after_value = console_tile[row][col+2:]
    insert_at_position(row, before_value, after_value, value)


def insert_at_position(row: int, 
                       before_value: str, 
                       after_value: str, 
                       value: str):
    console_tile[row] = before_value + value + after_value


def run():
    #print(r_npc.position)
    k.read_event()
    if k.is_pressed('a'):
        move_left()
        return
    if k.is_pressed('d'):
        move_right()
        return
    if k.is_pressed('w'):
        move_up()
        return
    if k.is_pressed('s'):
        move_down()
        return