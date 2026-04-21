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
global player_actor
player_actor = p.get_player()
global player_position
player_position = (4, 3)  # col 4, row 3
player_actor.position = player_position

def is_wall(col, row):
    if row < 0 or row >= len(test_print) or col < 0 or col >= 10:
        return True
    return test_print[row][col*2:col*2+2] == walls

def move_up():
    global test_print, player_position
    col, row = player_actor.position
    new_row = row - 1
    if is_wall(col, new_row):
        print("You can't move there")
    else:
        # clear old position
        test_print[row] = test_print[row][:col*2] + air + test_print[row][col*2+2:]
        # set new position
        test_print[new_row] = test_print[new_row][:col*2] + player + test_print[new_row][col*2+2:]
        player_actor.position = (col, new_row)
        player_position = player_actor.position

def move_down():
    global test_print, player_position
    col, row = player_actor.position
    new_row = row + 1
    if is_wall(col, new_row):
        print("You can't move there")
    else:
        # clear old position
        test_print[row] = test_print[row][:col*2] + air + test_print[row][col*2+2:]
        # set new position
        test_print[new_row] = test_print[new_row][:col*2] + player + test_print[new_row][col*2+2:]
        player_actor.position = (col, new_row)
        player_position = player_actor.position

def move_left():
    global test_print, player_position
    col, row = player_actor.position
    new_col = col - 1
    if is_wall(new_col, row):
        print("You can't move there")
    else:
        # clear old position
        test_print[row] = test_print[row][:col*2] + air + test_print[row][col*2+2:]
        # set new position
        test_print[row] = test_print[row][:new_col*2] + player + test_print[row][new_col*2+2:]
        player_actor.position = (new_col, row)
        player_position = player_actor.position

def move_right():
    global test_print, player_position
    col, row = player_actor.position
    new_col = col + 1
    if is_wall(new_col, row):
        print("You can't move there")
    else:
        # clear old position
        test_print[row] = test_print[row][:col*2] + air + test_print[row][col*2+2:]
        # set new position
        test_print[row] = test_print[row][:new_col*2] + player + test_print[row][new_col*2+2:]
        player_actor.position = (new_col, row)
        player_position = player_actor.position



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