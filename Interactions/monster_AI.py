from Interactions.player_interactions import clear_old_position, new_position_value, insert_at_position, console_tile, is_wall, message_wall, player_sprite, air_sprite
import Actors.npc_repository.listof_npc as n
import Actors.player as p
import monster_spawn.npc as npc

global player_position
col, row = p.player_instance.position
new_col, new_row = col, row
# nom = placeholder 

def Yplayer_distance():
    npc.position[1]-p.player_instance.position[1]==Yplayer_distance
    return Yplayer_distance(int)


def Xplayer_distance ():
    npc.position[0]-p.player_instance.position[0]==Xplayer_distance
    return Xplayer_distance(int)

def move_up():
    move(is_vertical=True, 
         is_negative=True)


def move_down():
    move(is_vertical=True, 
         is_negative=False)


def move_left():
    move(is_vertical=False, 
         is_negative=True)


def move_right():
    move(is_vertical=False, 
         is_negative=False)


def move(is_vertical: bool, is_negative: bool):
    """
    But: Permet de déplacer le joueur

    Entrées: 
        is_vertical: Verifie si le mouvement est vertical,
        is_negative: Vrai si le mouvement va vers le haut ou la gauche
    """


    if(is_vertical is True):
        new_row = new_position_value(row, is_negative)

    else:
        new_col = new_position_value(col, is_negative)

    if is_wall(new_col, new_row):
        message_wall()
        return
        
    clear_old_position(col, row)
    insert_at_position(new_col, new_row, npc.sprite)
    # monster position = (new_col, new_row)
    npc.position = (new_col, new_row)


# valeur par défaut pour les positions de monstre
col = -1
row = -1

while True:
    for i in console_tile:
        col =i.find(npc.sprite) 
        if col != -1:
            row = i
            break

        if 0<Xplayer_distance<5 and -2>Yplayer_distance>2:
            if npc.position[0]+1==p.player_instance.position[0] and npc.position[1] == p.player_instance.position[1]:
                break
            move_right()
            #move right
 
 
        if 0>Xplayer_distance>-5 and -2>Yplayer_distance>2:
            if npc.position[0]-1 == p.player_instance.position[0] and npc.position[1] == p.player_instance.position[1]:
                    break
            move_left()
            #move left
 
 
        if 0<Xplayer_distance<5 and -2<Yplayer_distance<2:
            if npc.position[1]+1 == p.player_instance.position[1] and npc.position[0] == p.player_instance.position[0]:
                break
            move_down()
            #move down
 
 
        if 0>Xplayer_distance>-5 and -2<Yplayer_distance<2:
            if npc.position[1]-1 == p.player_instance.position[1] and npc.position[0] == p.player_instance.position[0]:
                break
            move_up()
            #move_up