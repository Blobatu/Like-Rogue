# Marvyn Mbeugmo
# Ce module gère les différents niveaux du jeu en fonction de la progression du joueur.
# Il définit les caractéristiques de chaque niveau, telles que la taille, la difficulté et si le niveau est personnalisé ou non.

import sys
sys.path.append(r"c:\Users\Elitebook\OneDrive - Cegep de Sherbrooke\Documents\Sessiion 2\Programmation\Exercise et Projet\Projet 3")

from Progression import actor

levels = {
    'level_1' : {
        'size' : (16, 7),
        'difficulty' : 1,
        'custom' : False,
    },
    'level_2' : {
        'size' : (16, 7),
        'difficulty' : 3,
        'custom' : False,
    },
}

def get_current_level(player):
    """Retourne le niveau en fonction du level du joueur"""
    if player.level == 1:
        return levels['level_1']
    else:
        return levels['level_2']