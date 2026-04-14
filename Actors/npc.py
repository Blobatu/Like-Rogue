"""
Auteur : Luc Desforges
Date : 14 avril 2026
Description : TODO
"""
import Actors.actor as a
class NPC(a.Actor):
    
    def __init__(self,
                 zone: int, 
                 name: str,
                 sprite: str,
                 position: tuple[int, int], 
                 health: int, 
                 damage: int,
                 size: int):
        """
        description: Constructeur
        """
        super().__init__(name, sprite, position, health, damage, size)
        self.zone = zone
        
