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
    But:    Permet au joueur de se déplacer dans le donjon en écoutant les
            entrées du clavier (wasd pour les déplacements de base, 
            QE pour les déplacements diagonaux).
    """
    event = k.read_event()
    p_i.is_actor_on_bomb()
    p_i.bomb_counter()
    p_i.bomb_explodes()
    #print(event) # Debug: Affiche l'événement clavier pour vérifier les entrées
    if event.name == 'a':
        if event.event_type == k.KEY_DOWN and not is_pressed:
            #print("a pressed") # Debug: Affiche un message lorsque 'a' est pressé
            a_m.move_left()
            is_pressed = True # Set flag so it doesn't trigger again
        elif event.event_type == k.KEY_UP:
            is_pressed = False # Reset flag when released\
        return is_pressed
    if event.name == 'd':
        if event.event_type == k.KEY_DOWN and not is_pressed:
            a_m.move_right()  
            is_pressed = True # Set flag so it doesn't trigger again
        elif event.event_type == k.KEY_UP:
            is_pressed = False # Reset flag when released\
        return is_pressed
    if event.name == 'w':
        if event.event_type == k.KEY_DOWN and not is_pressed:
            a_m.move_up()
            is_pressed = True # Set flag so it doesn't trigger again
        elif event.event_type == k.KEY_UP:
            is_pressed = False # Reset flag when released\
        return is_pressed
    if event.name == 's':
        if event.event_type == k.KEY_DOWN and not is_pressed:
            a_m.move_down()
            is_pressed = True # Set flag so it doesn't trigger again
        elif event.event_type == k.KEY_UP:
            is_pressed = False # Reset flag when released\
        return is_pressed
    if event.name == 'q':
        if event.event_type == k.KEY_DOWN and not is_pressed:
            a_m.move_up()
            a_m.move_left()
            is_pressed = True # Set flag so it doesn't trigger again
        elif event.event_type == k.KEY_UP:
            is_pressed = False # Reset flag when released\
        return is_pressed
    if event.name == 'e':
        if event.event_type == k.KEY_DOWN and not is_pressed:
            a_m.move_down()
            a_m.move_right() 
            is_pressed = True # Set flag so it doesn't trigger again
        elif event.event_type == k.KEY_UP:
            is_pressed = False # Reset flag when released\
        return is_pressed
    if event.name == 'x':
        if event.event_type == k.KEY_DOWN and not is_pressed:
            aura_behavior.aura_damage(True)
            is_pressed = True # Set flag so it doesn't trigger again
        elif event.event_type == k.KEY_UP:
            is_pressed = False # Reset flag when released\
        return is_pressed
    if event.name == 'z':
        if event.event_type == k.KEY_DOWN and not is_pressed:
            a_m.p_i.drink_health_potion(5)
            is_pressed = True # Set flag so it doesn't trigger again
        elif event.event_type == k.KEY_UP:
            is_pressed = False # Reset flag when released\
        return is_pressed
    if event.name == 'b':
        if event.event_type == k.KEY_DOWN and not is_pressed:
            p_i.bomb_interaction()
            is_pressed = True # Set flag so it doesn't trigger again
        elif event.event_type == k.KEY_UP:
            is_pressed = False # Reset flag when released\
        return is_pressed
    print("Invalid key pressed") # Debug: Affiche un message pour les touches non reconnues

    return is_pressed
    # On vérifie les touches pressées pour 
    # déterminer la direction du déplacement
        
    
    