"""
Auteur : Luc Desforges
Date : 14 avril 2026
Description : TODO
"""
from . import actor as a

player_instance: Player = None
instanciated = False
class Player(a.Actor):

    def __init__(self, 
                 level: int,
                 damage_done: int,
                 damage_received: int,
                 name: str, 
                 sprite: str,
                 position: tuple[int, int], 
                 health: int = 1, 
                 damage: int = 1,
                 size: int = 1):
        """
        description: Constructeur
        """
        super().__init__(name, sprite, position, health, damage, size)
        self.level = level
        self.damage_done = damage_done
        self.damage_received = damage_received


def get_player():
    if(instanciated is False):
        player_instance = Player(level = 1, 
                                 damage_received = 0, 
                                 damage_done = 0,
                                 name = "Nard", 
                                 sprite = "@@",
                                 position = (0, 0))
    return player_instance