'''
auteur: Léonard Lefebvre
date:14 avril
description:to do
'''
import Actors.player as p
walls = ('# ')
player = '@ '
air = '. '
#player_position = player.position
mobs =("player","other_monsters")

test_print = "####################\n##. . . . . . . . ##\n##. . . . . . . . ##\n##. . . . . . . . ##\n##. . . . @ . . . ##\n##. . . . . . . . ##\n##. . . . . . . . ##\n####################"

player_actor = p.get_player()




def move_up():
    if (player_actor.position[0],player_actor.position[1]+1) == walls:
        print("You can't move there")
    else:
        player_actor.position=(player_actor.position[0],player_actor.position[1]+1)
def move_down():
    if (player_actor.position[0],player_actor.position[1]-1) == walls:
        print("You can't move there")
    else:
        player_actor.position=(player_actor.position[0],player_actor.position[1]-1)
def move_left():
    if (player_actor.position[0]-1,player_actor.position[1]) == walls:
        print("You can't move there")
    else:
        player_actor.position=(player_actor.position[0]-1,player_actor.position[1])
def move_right():
    if (player_actor.position[0]+1,player_actor.position[1]) == walls:
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