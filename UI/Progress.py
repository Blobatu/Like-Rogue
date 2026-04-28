class Progression:
    def __init__(self, name):
        # Nom du joueur
        self.name = name
        
        # Niveau de départ
        self.level = 1
        
        # XP actuel
        self.xp = 0
        
        # XP nécessaire pour monter niveau
        self.xp_to_next = 100

        # Message au début
        print(name, "commence au niveau 1")

    def gain_xp(self, success):
        # Si l'action est réussie
        if success:
            print("Action réussie +50 XP")
            
            # Ajouter 50 XP
            self.xp = self.xp + 50
        else:
            # Si l'action échoue
            print("Action échouée")

        # Vérifier si on peut monter de niveau
        if self.xp >= self.xp_to_next:
            
          # Augmenter le niveau
            self.level = self.level + 1
            
          # Enlever l'XP utilisé pour le niveau
            self.xp = self.xp - self.xp_to_next
            
          # Augmenter la difficulté (XP x1.5)
            self.xp_to_next = int(self.xp_to_next * 1.5)

          # Message de niveau gagné
            print("Bravo ! Niveau", self.level)

    def afficher(self):
        # Affiche les informations du joueur
        print("Nom :", self.name)
        print("Niveau :", self.level)
        print("XP :", self.xp, "/", self.xp_to_next)


# TEST DU PROGRAMME
if __name__ == "__main__":
    
    # Créer un joueur
    joueur = Progression("Nard")

    # Simuler des actions
    joueur.gain_xp(True)   # réussite
    joueur.gain_xp(True)   # réussite
    joueur.gain_xp(False)  # échec

    # Afficher les stats finales
    joueur.afficher()