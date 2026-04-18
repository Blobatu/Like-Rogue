scale_unit = 1
difficulty = 1


# une valeur '1' est équivalent à la health/damage --
# nécéssaire pour tuer en 1 coup un 'goblin' ou 'weak creature'.
# Si le scale_unit == 2, ça veut dire qu'un 'goblin' a 2 de 'health'
def scale(number: int):
    return scale_unit * number