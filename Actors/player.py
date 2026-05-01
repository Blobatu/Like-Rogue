"""
Auteur : Luc Desforges
Date : 14 avril 2026
Description : TODO
"""
from . import actor as a

class Player(a.Actor):
    def __init__(self, 
                 weapon: Weapon,
                 potion_count: int,
                 bomb_count: int,
                 level: int,
                 damage_done: int,
                 damage_received: int,
                 name: str, 
                 sprite: str,
                 position: tuple[int, int], 
                 health: int = 10, 
                 damage: int = 1,
                 size: int = 1):
        """
        description: Constructeur
        """
        super().__init__(name, sprite, position, health, damage, size)
        self.level = level
        self.damage_done = damage_done
        self.damage_received = damage_received
        self.weapon = weapon
        self.potion_count = potion_count
        self.bomb_count = bomb_count


player_instance: Player = Player(weapon=None,
                                 potion_count=3,
                                 bomb_count=5,
                                 level=1, 
                                 damage_received=0, 
                                 damage_done=0,
                                 name="Nard", 
                                 sprite="@ ",
                                 position=(0, 0))


class Weapon:
    def __init__(self, name: str,):
        self.name = name
