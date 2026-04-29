from . import player_interactions as p_i
from Actors import player as p
from Actors import npc
from .random_npc import r_npc

# nom = placeholder 

def Xplayer_distance():
    return r_npc.position[1] - p.player_instance.position[1]


def Yplayer_distance():
    return r_npc.position[0] - p.player_instance.position[0]

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
    But: Permet de déplacer le npc

    Entrées: 
        is_vertical: Verifie si le mouvement est vertical,
        is_negative: Vrai si le mouvement va vers le haut ou la gauche
    """
    col, row = r_npc.position
    new_col, new_row = col, row

    if(is_vertical is True):
        new_row = p_i.new_position_value(row, is_negative)

    else:
        new_col = p_i.new_position_value(col, is_negative)

    if p_i.is_wall(new_col, new_row):
        p_i.message_wall()
        return
        
    p_i.move_at_position(col, row, p_i.air_sprite)
    p_i.move_at_position(new_col, new_row, r_npc.sprite)
    # monster position = (new_col, new_row)
    r_npc.position = (new_col, new_row)
    if(r_npc.position[0] + 1 == p.player_instance.position[0] 
       and (r_npc.position[1] == p.player_instance.position[1] or
            r_npc.position[1] + 1 == p.player_instance.position[1] or
            r_npc.position[1] - 1 == p.player_instance.position[1]) or                         
       r_npc.position[0] - 1 == p.player_instance.position[0]
       and (r_npc.position[1] == p.player_instance.position[1] or
            r_npc.position[1] + 1 == p.player_instance.position[1] or
            r_npc.position[1] - 1 == p.player_instance.position[1]) or
       r_npc.position[0] == p.player_instance.position[0] 
       and (r_npc.position[1] + 1 == p.player_instance.position[1] or
            r_npc.position[1] - 1 == p.player_instance.position[1])
    ):
        print("Combat !")
        print("player position : " + str(p.player_instance.position))
        print("monster position : " + str(r_npc.position))


# valeur par défaut pour les positions de monstre


def algorithm():
    col_wow = -1
    row_wow = -1
    row_count = -1
    for i in p_i.console_tile:
        row_wow += 1
        col_wow = i.find(r_npc.sprite) 
        if col_wow == -1:
            continue
        if col_wow != -1:
            row_wow = row_count
        
        if -2 < Yplayer_distance() <2 and -4 < Xplayer_distance() < 0:
            if r_npc.position[0] + 1 == p.player_instance.position[0] and r_npc.position[1] == p.player_instance.position[1]:
                break
            move_down()
            if r_npc.position[0] - 1 == p.player_instance.position[0] and r_npc.position[1] == p.player_instance.position[1]:
                break
            #move down
 
 
        if -2 < Yplayer_distance() <2 and 0 < Xplayer_distance() < 4:
            if r_npc.position[0] - 1 == p.player_instance.position[0] and r_npc.position[1] == p.player_instance.position[1]:
                    break
            move_up()
            if r_npc.position[0] - 1 == p.player_instance.position[0] and r_npc.position[1] == p.player_instance.position[1]:
                break
            #move up
 
 
        if -2 < Xplayer_distance() < 2 and -4 < Yplayer_distance() < 0:
            if r_npc.position[0] - 1 != p.player_instance.position[0]:
                move_right()
            break

            #move right
 
 
        if -2 < Xplayer_distance() < 2 and 0 < Yplayer_distance() < 4:
            if r_npc.position[1] + 1 != p.player_instance.position[1]:
                
                move_left()
            break
            
            #move_left