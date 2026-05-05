"""
Auteur : Luc Desforges
Date : 1 mai 2026
Description : Classe pour les NPCs du jeu, héritant de la classe Actor.
"""
from . import actor as a

class NPC(a.Actor):
    def __init__(self,
                 aura: int,
                 name: str,
                 sprite: str,
                 position: tuple[int, int] = (0, 0), 
                 health: int = 1, 
                 damage: int = 1):
        """
        description: Constructeur
        """
        super().__init__(name, sprite, position, health, damage)
        self.aura = aura