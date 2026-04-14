'''
auteur: Léonard Lefebvre
date:14 avril
description:to do
'''

test_print = (". ##. . @ . . \n. . ##. . . . . . .")
print(test_print)

walls = ('#')
player = '@'
#player_position = player.position
mobs =("player","other_monsters")



stay = "stay"
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



    
def current_position():
    for mobs_position in mobs:
        return mobs_position
    

def loop_back():
    for mobs_position in mobs:
        last_positions = mobs_position
    return mobs_position

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
    

