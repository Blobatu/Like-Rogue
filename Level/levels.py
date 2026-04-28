# Marvyn Mbeugmo
# Ce module gère les différents niveaux du jeu en fonction de la progression du joueur.
# Il définit les caractéristiques de chaque niveau, telles que la taille, la difficulté et si le niveau est personnalisé ou non.

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
    'level_3' : {
        'size' : (16, 7),
        'difficulty' : 5,
        'custom' : False,
    },
    'level_4' : {
        'size' : (16, 7),
        'difficulty' : 7,
        'custom' : False,
    },
}

def get_current_level(player):
    """Retourne le niveau en fonction du level du joueur"""
    if player.level == 1:
        return levels['level_1']
    else:
        return levels['level_2']