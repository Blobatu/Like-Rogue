"""
Auteur : Léonard  & Luc Desforges
Date : 1 mai 2026
Description : Module pour la gestion des déplacements du joueur dans le jeu.
"""
from . import actor_movement as a_m
import keyboard as k

def listen_to_keyboard():
    """
    But:    Permet au joueur de se déplacer dans le donjon en écoutant les
            entrées du clavier (wasd pour les déplacements de base, 
            QE pour les déplacements diagonaux).
    """
    k.read_event()
    # On vérifie les touches pressées pour 
    # déterminer la direction du déplacement

    if k.is_pressed('a'):
        a_m.move_left()
        return
    if k.is_pressed('d'):
        a_m.move_right()  
        return
    if k.is_pressed('w'):
        a_m.move_up()
        return
    if k.is_pressed('s'):
        a_m.move_down()
        return
    if k.is_pressed('q'):
        a_m.move_up()
        a_m.move_left()
        return
    if k.is_pressed('e'):
        a_m.move_down()
        a_m.move_right()
        return
    