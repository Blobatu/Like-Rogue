"""
Auteur : Luc Desforges
Date : 1 mai 2026
Description : Classe de base pour les acteurs du jeu, incluant le joueur et les NPCs.
"""
import public

class Actor:
    def __init__(self, 
                 name: str,
                 sprite: str,
                 position: tuple[int, int], 
                 health: int, 
                 damage: int,
                 size: int):
        """
        description: Constructeur
        """
        self.name = name
        self.sprite = sprite
        self.position = position
        self.health = public.scale(health)
        self.damage = public.scale(damage)
        self.size = size

        self.max_health = public.scale(health)


    def lose_life(self, amount: int):
        print(f"You lost {amount} health points!")
        self.health -= public.scale(amount)
        print(f"Health:{self.health}/{self.max_health}")

        if(self.health <= 0):
            self.health = 0
            return True
        return False


    def is_alive(self) -> bool:
        return self.health > 0
    

    def set_position(self, position: tuple[int, int]):
        self.position = position
        print(self.position)


    def set_position(self, col: int, row: int):
        self.position = (col, row)
        print(self.position)


    def get_col(self):
        return self.position[0]
    

    def get_row(self):
        return self.position[1]
