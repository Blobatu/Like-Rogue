''' 
Ce programme gère l'affichage d'une barre de progression pour un personnage dans un jeu vidéo.
Sa agit comme une interface utilisateur pour montrer l'expérience (XP) actuelle du personnage par rapport à l'expérience maximale nécessaire pour atteindre le niveau suivant.
Marvyn Mbeugmo 
'''
def afficher_barre(xp, xp_max):
    '''Affiche une barre de progression visuelle pour représenter l'expérience actuelle du personnage.'''
    progression = int((xp / xp_max) * 20)
    barre = "[" + "#" * progression + "-" * (20 - progression) + "]"
    print(barre)