import random as r
from pathlib import Path
"""
author : emmanuel Bissonnette
Goal : ce fichier contien les fonctions dinteraction avec les props 

"""

DATA_DIR = Path(__file__).resolve().parent

def chest(player_interaction):
    if player_interaction == True:
        item = r.randint(0, 3)
        file_path = DATA_DIR / "chest_item_list"
        with open(file_path, "r", encoding="utf-8") as file:
            items = file.readlines()
        item = items[item].strip()
        return item, "break_chest"

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