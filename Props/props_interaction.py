import random as r
import pygame,time 
from Actors import player as p
from Actors import npc_database as npc_db
import asyncio
from Interactions import dungeon
import public
from Interactions import actor_movement as am
#from UI.UI import Button
"""
author : emmanuel Bissonnette
Goal : ce fichier contien les fonctions dinteraction avec les props 

"""


def chest():
        item = r.randint(0,3)
        path = "Props/chest_item_list"
        file = open(path)
        lines = file.readlines()
        item = lines[item]
        item.strip()
        file.close()
        if item != "health_pot":
           current_weapon = p.player_instance.weapon
           awnser = input(f"Vous avez trouve {item} voulez vous remplacer votre {current_weapon} Y ou N")
           if awnser == "Y" :
                p.player_instance.weapon = item
           elif awnser == "N":
                p.player_instance.weapon = current_weapon
        else:
             p.player_instance.health += public.scale(5)
    
    
def barrel ():
    
    pass
def door ():
   p.player_instance.level +=1 
def spike_trap():
        p.player_instance.lose_life(r.randint(1,3))
def void ():
        remaining_life = p.player_instance.health
        p.player_instance.lose_life(remaining_life)
        
def interaction_check(player_pos:str):
    match player_pos:
        case "▤ ":
            chest()
        case "⩉ ":
            barrel()
        case "| ":
            door()
        case "△ ":
            spike_trap()
        case "  ":
            void()     
async def bomb_interaction():
    if p.player_instance.bomb_count > 0:
        p.player_instance.bomb_count -= 1
        bomb_position = p.player_instance.position
        await asyncio.sleep(r.randint(2,5))
        player_bomb_check = (p.player_instance.position[0]+5,p.player_instance.position[1]-5)
        if player_bomb_check[0] < bomb_position[0] > player_bomb_check[1] and player_bomb_check[0]<bomb_position[1]>player_bomb_check[1]:
            p.player_instance.lose_life(r.randint(1,3))
        for key,npc in npc_db.listof_dbnpc.items():
            if npc.position[0] < bomb_position[0] > npc.position[1] and npc.position[0]<bomb_position[1]>npc.position[1]:
                npc.lose_life(r.randint(1,5))
        am.replace_around_position(bomb_position[0],bomb_position[1],3,dungeon.air_sprite)
        
    
    
    

