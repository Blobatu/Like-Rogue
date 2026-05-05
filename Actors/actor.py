"""
Auteur : Luc Desforges
Date : 1 mai 2026
Description :   Classe de base pour les acteurs du jeu, 
                incluant le joueur et les NPCs.
"""
import public

class Actor:
    def __init__(self, 
                 name: str,
                 sprite: str,
                 position: tuple[int, int], 
                 health: int, 
                 damage: int):
        """
        description: Constructeur
        """
        self.name = name
        self.sprite = sprite
        self.position = position
        self.health = public.scale(health)
        self.damage = public.scale(damage)

        self.max_health = public.scale(health)


    def lose_life(self, amount: int):
        """
        But: Inflige des dégâts à l'acteur et vérifie s'il est mort.
        Entrée: 
            amount (int) - la quantité de dégâts à infliger.
        Sortie:
            bool - True si l'acteur est mort, False sinon.
        """
        print(f"You lost {amount} health points!")
        self.health -= public.scale(amount)
        print(f"Health:{self.health}/{self.max_health}")

        if(self.health <= 0):
            self.health = 0
            return True
        return False


    def is_alive(self) -> bool:
        """
        But: Vérifie si l'acteur est encore en vie.
        Sortie: bool - True si l'acteur est en vie, False sinon.
        """
        return self.health > 0


    def set_position(self, col: int, row: int):
        """
        But: Met à jour la position de l'acteur.
        Entrée: 
            col (int) - la nouvelle colonne de l'acteur,
            row (int) - la nouvelle rangée de l'acteur.
        """
        self.position = (col, row)
        #print(self.position)


    def get_col(self):
        """
        But: Récupère la colonne actuelle de l'acteur.
        Sortie: int - la colonne actuelle de l'acteur.
        """
        return self.position[0]
    

    def get_row(self):
        """
        But: Récupère la rangée actuelle de l'acteur.
        Sortie: int - la rangée actuelle de l'acteur.
        """
        return self.position[1]
