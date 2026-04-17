"""
Auteur : Luc Desforges
Date : 14 avril 2026
Description : TODO
"""
from . import actor as a
class NPC(a.Actor):
    
    def __init__(self,
                 zone: int,
                 name: str,
                 sprite: str,
                 position: tuple[int, int] = (0, 0), 
                 health: int = 1, 
                 damage: int = 1,
                 size: int = 1):
        """
        description: Constructeur
        """
        super().__init__(name, sprite, position, health, damage, size)
        self.zone = zone
        
