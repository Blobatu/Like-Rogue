import random as r
""""
author : emmanuel Bissonnette
Goal : ce fichier contien les fonctions dinteraction avec les props 

"""

def chest(player_interaction):
    if player_interaction == True:
        item = r.randint(0,3)
    else:
        return()
    
    file = open("chest_item_list")
    file = file.readlines()
    item = file[item]
    return (item,"break_chest")
def barrel ():
    pass
def door ():
    pass