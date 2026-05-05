"""
Auteur : Léonard  & Luc Desforges
Date : 1 mai 2026
Description : Module pour la gestion des déplacements du joueur dans le jeu.
"""

from Interactions import aura_behavior

from . import actor_movement as a_m
from Props import props_interaction as p_i
import keyboard as k

def listen_to_keyboard(is_pressed: bool):
    """
    But:    Écoute les touches du clavier du joueur, e qui permet 
            de se déplacer dans le donjon,
            d'attaquer les monstres, 
            de déposer des bombes et, 
            de boire des potions de vie
    """
    event = k.read_event()
    # Regarde si une ou plusieurs bombes sont déposés
    # et calcule si elle(s) explosent
    p_i.is_actor_on_bomb()
    p_i.bomb_counter()
    p_i.bomb_explodes()

    if event.name == 'a':
        if is_keydown(event, is_pressed):
            a_m.move_left()
            is_pressed = True
        elif is_keyup(event):
            is_pressed = False
        return is_pressed
    if event.name == 'd':
        if is_keydown(event, is_pressed):
            a_m.move_right()  
            is_pressed = True
        elif is_keyup(event):
            is_pressed = False
        return is_pressed
    if event.name == 'w':
        if is_keydown(event, is_pressed):
            a_m.move_up()
            is_pressed = True
        elif is_keyup(event):
            is_pressed = False
        return is_pressed
    if event.name == 's':
        if is_keydown(event, is_pressed):
            a_m.move_down()
            is_pressed = True
        elif is_keyup(event):
            is_pressed = False
        return is_pressed
    if event.name == 'q':
        if is_keydown(event, is_pressed):
            a_m.move_up()
            a_m.move_left()
            is_pressed = True
        elif is_keyup(event):
            is_pressed = False
        return is_pressed
    if event.name == 'e':
        if is_keydown(event, is_pressed):
            a_m.move_down()
            a_m.move_right() 
            is_pressed = True
        elif is_keyup(event):
            is_pressed = False
        return is_pressed
    if event.name == 'x':
        if is_keydown(event, is_pressed):
            aura_behavior.aura_damage(True)
            is_pressed = True
        elif is_keyup(event):
            is_pressed = False
        return is_pressed
    if event.name == 'z':
        if is_keydown(event, is_pressed):
            a_m.p_i.drink_health_potion(5)
            is_pressed = True
        elif is_keyup(event):
            is_pressed = False
        return is_pressed
    if event.name == 'b':
        if is_keydown(event, is_pressed):
            p_i.bomb_interaction()
            is_pressed = True
        elif is_keyup(event):
            is_pressed = False
        return is_pressed

    return is_pressed
    # On vérifie les touches pressées pour 
    # déterminer la direction du déplacement
        
def is_keydown(event, is_pressed: bool):
    return event.event_type == k.KEY_DOWN and not is_pressed

def is_keyup(event):
    return event.event_type == k.KEY_UP
    