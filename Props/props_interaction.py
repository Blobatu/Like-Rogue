import random as r
""""
author : emmanuel Bissonnette
Goal : ce fichier contien les fonctions dinteraction avec les props 

"""

def chest(player_interaction):
    if player_interaction == True:
        item = r.randint(0,3)
        file = open("chest_item_list")
        file = file.readlines()
        item = file[item]
        return (item,"break_chest")

    else:
        return()
    
    
def barrel ():
    pass
def door ():
    pass
def spike_trap(player_interaction,health):
    if player_interaction == True:
        health = health - r.randint(1,10)
        return health
    else:
        return health
def void (player_interaction,health):
    if player_interaction == True:
        health == 0
        return health
    else:
        return health