# Marvyn Mbeugmo
# Ce module gère les différents niveaux du jeu en fonction de la progression du joueur.
# Il définit les caractéristiques de chaque niveau, telles que la taille, la difficulté et si le niveau est personnalisé ou non.

levels = {
    'level_1' : {
        'size' : (16, 3),
        'difficulty' : 8,
        'custom' : False,
    },
    'level_2' : {
        'size' : (16, 4),
        'difficulty' : 10,
        'custom' : False,
    },
    'level_3' : {
        'size' : (16, 5),
        'difficulty' : 12,
        'custom' : False,
    },
    'level_4' : {
        'size' : (16, 6),
        'difficulty' : 14,
        'custom' : False,
    },
}

def get_current_level(player):
    """Retourne le niveau en fonction du level du joueur"""
    if player.level == 1:
        return levels['level_1']
    else:
        return levels['level_2']