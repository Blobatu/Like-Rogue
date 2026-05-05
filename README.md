# Like-Rogue
projet 3 de prog 1

## dépendances
imports externes nécéssaires:
- pygame community edition
- pygame-menu comunity edition
- keyboard

pour les installer:
```cmd
py -3.14 -m pip install pygame-ce
py -3.14 -m pip install pygame-menu-ce
py -3.14 -m pip install keyboard
```

## Niveaux et progression
### Niveaux
Tous les niveaux sont générés aléatoirement de manière à ce que chaque partie soient uniques.
### Progression
Une fois que vous avez tué assez d'ennemis, une porte "|" s'ouvrira et vous pourrez passer au prochain niveau.
## Interactions avec le jeux
Avant le premier mouvement le joueur est invisible et apparait toujours dans le haut en gauche de l'écran. 
### Contrôles
**Déplacement**: le joueurs fonctionne avec le controle WASD

*W* Déplacement vers le haut

*A* Déplacement vers la gauche

*S* Déplacement vers le bas

*D* Déplacement vers la droite

Voici d'autres commandes pour les actions supplémentaires qui ne sont pas des déplacements

*X* Attaquer

*Z* Boire une potion

*B* Déposer une bombe

### Interactions avec les monstres
---

### Déplacement

Chaque déplacement ennemi est lié a un algorithme qui réagit selon la distance entre le monstre et le joueur

### Les monstres

Chaque monstre a une particularité et une apparence sur l'interface
___
Nom: Goblin

Apparence sur l'interface: ¤ 

Vie: 1

Zone de dégats: 1

Dégats: 1
____
Nom: Aura Farmer

Apparence sur l'interface: Ω

Vie: 2

Zone de dégats: 3

Dégats: 1
____
Nom: Orc

Apparence sur l'interface: Θ

Vie: 2

Zone de dégats: 2

Dégats: 2

___


# Jeu par:
- **Luc Desforges** - joueur et ennemies - organisation générale
- **Antoine D-C** - génération de niveaux
- **Léonard Lefebvre** - interactions des joueur et ennemies
- **Emmanuel Bissonnette** - interactions des objets
- **James Bergeron** - interface visuel
- **Marvyn Mbeugmo** - progression
