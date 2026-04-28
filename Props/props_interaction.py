import random as r
import pygame,time 
from Actors import player as p

#from UI.UI import Button
"""
author : emmanuel Bissonnette
Goal : ce fichier contien les fonctions dinteraction avec les props 

"""


def chest():
        item = r.randint(0,3)
        path = "Props/chest_item_list"
        file = open(path)
        file = file.readlines()
        item = file[item]
        item.strip()
        if item != "health_pot":
           current_weapon = p.player_instance.weapon
           awnser = input(f"Vous avez trouve {item} voulez vous remplacer votre {current_weapon} Y ou N")
           if awnser == "Y" :
                p.player_instance.weapon = item
           elif awnser == "N":
                p.player_instance.weapon = current_weapon
        else:
             p.player_instance.health +=5
    
    
def barrel ():
    
    pass
def door ():
   p.player_instance.level +=1 
def spike_trap():
        p.player_instance.lose_life(r.randint(3,10))
def void ():
        remaining_life = p.player_instance.health
        p.player_instance.lose_life(remaining_life)
        
def interaction_check(player_pos:str):
    match player_pos:
        case "[]":
            chest()
        case "()":
            barrel()
        case "||":
            door()
        case "△ ":
            spike_trap()
        case "  ":
            void()     
async def bomb_interaction():
    bomb_position = p.player_instance.position
    await timer(r.randint(5,10))
    player_bomb_check = (p.player_instance.position[0]+5,p.player_instance[1]-5)
    if bomb_position[0] < player_bomb_check[0] and bomb_position[1]>player_bomb_check[1]:
         print("yay")
    pass
async def timer(time_sleep):
        time.sleep(time_sleep)
        print("bananasleep")
    


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