"""

"""


# import

from tileset import tileset as ts
import random as rd

# fonctions

def make_lvl_data(maze):
    """
    gets a list from the maze generator and stitches rooms together to create the actual level data
    in: list of lists of rooms from maze generator
    out: list of strings, each list is a line of the level
    """
    lvl_data = []
    for line in maze:
        for i in range(1, 8):
            lvl_data.append('')
            for room in line:
                if room =='':
                    room = 'void'   
                lvl_data[-1] += ts[room][i]
    return lvl_data


def print_room(maze):
    """
    prints the actual level as it will appears in the game
    in: list of lists of rooms from maze generator
    out: lines of the level being printed out one by one
    """
    for i in make_lvl_data(maze):
        print(i)
    
    
def print_room_as_list(maze):
    """
    to debug, simply prints the result of maze_to_lvl_data, kinda useless but has clear labeling
    in: list of lists of rooms from maze generator
    out: list of strings, each list is a line of the level 
    """
    print(make_lvl_data(maze))


# test

fullscreen_layout_template = [[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16], [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16], [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16], [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16], [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16], [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16], [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]]
test_1 = [['end_b','','','','crnr_rb','3way_lrb','3way_lrb','strgt_horz','end_l','crnr_wall_rb','wall_t','crnr_wall_lb','crnr_rb','3way_lrb','crnr_lb',''], ['strgt_vert','','end_r','3way_lrb','crnr_lt','crnr_rt','cross-rb','wall_t','wall_t','empty+lt','pillar','empty+rt','cross-lb','cross_pillar','3way_ltb',''], ['3way_rtb','strgt_horz','strgt_horz','cross','strgt_horz','3way_lrb','door_l','empty','empty','empty','empty','empty','cross-lt','3way_lrt','crnr_lt',''], ['3way_ltb','crnr_wall_rb','wall_t','door_t','crnr_wall_lb','end_t','wall_l','empty','full','full','empty','empty','end_t','crnr_wall_rb','wall_t','crnr_wall_lb'], ['strgt_vert','crnr_wall_rt','door_b','empty+lb','door_r','crnr_lb','wall_l','empty','empty','empty+rb','wall_b','empty+lb','empty','empty','empty','wall_r'], ['strgt_vert','hollow','strgt_vert','crnr_wall_rt','crnr_wall_lt','strgt_vert','crnr_wall_rt','door_b','wall_b','crnr_wall_lt','crnr_rb','cross-rt','wall_b','empty+lb','empty','wall_r'], ['crnr_rt','strgt_horz','3way_lrt','strgt_horz','strgt_horz','3way_lrt','strgt_horz','crnr_lt','','crnr_rb','3way_lrt','3way_lrt','end_l','crnr_wall_rt','wall_b','crnr_wall_lt']]

#print_room(test_1)
#print_room_as_list(test_1)

