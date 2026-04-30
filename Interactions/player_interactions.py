'''
Auteur: Léonard Lefebvre
Date: 14 avril
Description: to do
'''

from Actors.player import player_instance as p_i
from Level.level_generation import full_level as fl
from . import actor_movement as a_m
import keyboard as k

#player_position = player.position
mobs = ("player","other_monsters")

global player_position
player_position = (3, 24)  # col 5, row 3
p_i.position = player_position

def run():
    k.read_event()
    print(f"player  : {p_i.position}")
    if k.is_pressed('a'):
        a_m.move_left()
        return
    if k.is_pressed('d'):
        a_m.move_right()  
        return
    if k.is_pressed('w'):
        a_m.move_up()
        return
    if k.is_pressed('s'):
        a_m.move_down()
        return
    