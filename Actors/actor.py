"""
Auteur : Luc Desforges
Date : 14 avril 2026
Description : TODO
"""
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
        self.health = health
        self.damage = damage
        self.size = size

        self.max_health = health

    def lose_life(self, amount: int):
        self.health -= amount
        print(f"Health:{self.health}/{self.max_health}")
        if(self.health <= 0):
            self.health = 0
            print(f"{self.name} is dead")
            return True
        return False
    
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
