'''
auteur: Léonard Lefebvre
date:14 avril
description:to do
'''
import Actors.player as p
walls = "##"
player = "@ "
air = ". "
#player_position = player.position
mobs =("player","other_monsters")

global test_print
test_print = ["####################",
              "##. . . . . . . . ##",
              "##. . . . . . . . ##",
              "##. . . . @ . . . ##",
              "##. . . . . . . . ##",
              "####################"]

# position du player pour les tests, à enlever plus tard

global player_position
player_position = (5, 3)  # col 5, row 3
p.player_instance.position = player_position


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
    global test_print, player_position
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
    set_new_position(new_col, new_row)
    p.player_instance.position = (new_col, new_row)
    player_position = p.player_instance.position


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
    if(col < 0 or col >= 10):
        return True
    if(row < 0 or row >= len(test_print)):
        return True
    if(test_print[row][col*2:col*2+2] == walls):
        return True
        
    return False


def message_wall():
    print("You can't move there")


def clear_old_position(col: int, row: int):
    insert_at_position(col, row, air)


def set_new_position(col: int, row: int):
    insert_at_position(col, row, player)


def insert_at_position(col: int, row: int, value: str):
    test_print[row] = test_print[row][:col*2] + value + test_print[row][col*2+2:]

"""
def move_left():
    global test_print
    
    pos = test_print.index(player)
    if test_print[pos-2] == '#':
        print("You can't move there")
    else:
        chars = list(test_print)
        chars[pos] = air
        chars[pos-2] = player
        test_print = "".join(chars)
    
    
def move_right():
    global test_print
    
    pos = test_print.index(player)
    if test_print[pos+2] == '##':
        print("You can't move there")
    else:
        chars = list(test_print)
        chars[pos] = air
        chars[pos+2] = player
        test_print = "".join(chars)
def move_up():
    global test_print
    
    test_print.splitlines()
    
    for lines in test_print.splitlines():
        if player in lines:
            pos = lines.index(player)
            if test_print[test_print.index(lines)-len(lines)+pos] == walls:
                print("You can't move there")
            else:
                chars = list(test_print)
                chars[test_print.index(lines)+pos] = air
                chars[test_print.index(lines)-len(lines)+pos-1] = player
                test_print = "".join(chars)
def move_down():
    global test_print
    test_print.splitlines()
    for lines in test_print.splitlines():
        if player in lines:
            pos = lines.index(player)
            if test_print[test_print.index(lines)+len(lines)+pos] == '#':
                print("You can't move there")
            else:
                chars = list(test_print)
                chars[test_print.index(lines)+pos] = air
                chars[test_print.index(lines)+len(lines)+pos+1] = player
                test_print = "".join(chars)
"""


while True:
    print('\n'.join(test_print))
    movements = input("up, down, left, right: ")
    if movements == "left":
        move_left()
    elif movements == "right":
        move_right()
    elif movements == "up":
        move_up()
    elif movements == "down":
        move_down()