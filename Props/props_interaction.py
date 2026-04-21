import random as r
import pygame as pg
import Actors.player as player
from UI.UI import Button
"""
author : emmanuel Bissonnette
Goal : ce fichier contien les fonctions dinteraction avec les props 

"""


def chest(player:player.Player):
        item = r.randint(0,3)
        path = "Props/chest_item_list"
        file = open(path)
        file = file.readlines()
        item = file[item]
        item.strip()
        if item != "health_pot":
           current_weapon = player.weapon
           while True:
                pass
        else:
             player.health +=5
    
    
def barrel ():
    pass
def door (player:player.Player):
    player.level +=1 
def spike_trap(player:player.Player):
        player.lose_life(r.randint(3,10))
def void (player:player.Player):
        remaining_life = player.health
        player.lose_life(remaining_life)
        
def interaction_check(player_pos):
    if False:
        for item in props:
            if item == player_pos:
                current_prop = item
                break
            else:
                pass
    _player = player.get_player()
    match player_pos:
        case "[]":
            chest(_player)
        case "()":
            barrel(_player)
        case "||":
            door(_player)
        case "△.":
            spike_trap(_player)
        case "  ":
            void(_player)                    

chest_dic = {

    "sprite":"[]",
    "interaction": chest,
    


}
barrel_dic = {
    "sprite":"()",
    "interaction": barrel,


}
door_dic = {
    "sprite":"||",
    "interaction": door,

}
spike_trap_dic = {
    
    "sprite":"△",
    "interaction": spike_trap,
}
void_dic = {
    "sprite":" ",
    "interaction": void,
}
props = {

    "[]":chest_dic,
    "()":barrel_dic,
    "||":door_dic,
    "△":spike_trap_dic,
    " ":void_dic,



}
interaction_check("[]")