'''
auteur: Léonard Lefebvre
date:14 avril
description:to do
'''
import Actors.player as p
walls = '##'
player = '@ '
air = '. '
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
global player_actor
player_actor = p.get_player()
global player_position
player_position = (10, 3) 
player_actor.position = player_position



def move_up():
    global test_print, player_position
    if (player_actor.position[0],player_actor.position[1]+1) == walls:
        print("You can't move there")

    else:
        chars = test_print

        print(player_actor.position)
        chars = list(chars[player_actor.position[1]-1])
        chars[player_actor.position[0]] = player
        player_actor.position=(player_actor.position[0],player_actor.position[1]-1)
        player_position = player_actor.position
        test_print[player_actor.position[1]] = "".join(chars)
        print(player_actor.position)
def move_down():
    global test_print, player_position
    if (player_actor.position[0],player_actor.position[1]-1) == walls:
        print("You can't move there")
    else:
        player_actor.position=(player_actor.position[0],player_actor.position[1]-1)
def move_left():
    global test_print, player_position
    if (player_actor.position[0]-1,player_actor.position[1]) == walls:
        print("You can't move there")
    else:
        player_actor.position=(player_actor.position[0]-1,player_actor.position[1])
def move_right():
    global test_print, player_position
    new_row = player_actor.position[0]
    new_col = player_actor.position[1] + 1
    if player_actor.position == (player_actor.position[0]+1,player_actor.position[1])== walls:
        print("You can't move there")
    else:
        player_actor.position=(player_actor.position[0]+1,player_actor.position[1])



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
    print(test_print)
    movements = input("up, down, left, right: ")
    if movements == "left":
        move_left()
    elif movements == "right":
        move_right()
    elif movements == "up":
        move_up()
    elif movements == "down":
        move_down()