'''
auteur: Léonard Lefebvre
date:14 avril
description:to do
'''
# ligne 7 a 10 test pour l'instant
import sys,os
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)
from Level.tileset import tileset as ts
from Level.level_generation import make_lvl_data as ld, print_room as pr


test_print = ld.make_lvl_data(7,16)
print(test_print)

walls = ('#')
player = '@'
#player_position = player.position
mobs =("player","other_monsters")



def move_left():
    global test_print
    
    pos = test_print.index(player)
    if test_print[pos-2] == '#':
        print("You can't move there")
    else:
        chars = list(test_print)
        chars[pos] = "."
        chars[pos-2] = player
        test_print = "".join(chars)
        print(test_print)
    
    
def move_right():
    global test_print
    
    pos = test_print.index(player)
    if test_print[pos+2] == '#':
        print("You can't move there")
    else:
        chars = list(test_print)
        chars[pos] = "."
        chars[pos+2] = player
        test_print = "".join(chars)
        print(test_print)


while True:
    movements = input("up, down, left, right: ")
    if movements == "left":
        move_left()
    elif movements == "right":
        move_right()
    elif movements == "up":
        move_up()
    elif movements == "down":
        move_down()
    

