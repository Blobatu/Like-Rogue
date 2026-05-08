# Like-Rogue
projet 3 de prog 1

## Dépendances
imports externes nécéssaires:
- pygame community edition
- pygame-menu comunity edition
- keyboard

Pour les installer:
```cmd
py -3.14 -m pip install pygame-ce
py -3.14 -m pip install pygame-menu-ce
py -3.14 -m pip install keyboard
```
## Démarrer
- Ajustez la taille de police de votre terminal
<img width="1537" height="542" alt="image" src="https://github.com/user-attachments/assets/2a16e2ed-acf5-4e02-9c25-0959b822a0e1" />

- Faites la commande suivante sur votre clavier pour avoir un terminal dans une autre fenêtre:
  - Ctrl+Alt+Shift+`
- Maximizez la nouvelle fenêtre
- Inscrivez la commande suivante dans votre terminal
  - py main.py
<img width="806" height="113" alt="image" src="https://github.com/user-attachments/assets/16eb6405-b02d-416f-a21e-cf9d944e3413" />

- Vous pouvez maintenant jouer au jeu
<img width="1918" height="1106" alt="image" src="https://github.com/user-attachments/assets/510807d8-b344-459f-bed8-947c54c5bbbf" />

## Interface visuel
### Le fonctionnement du code/but
Le but du code dans UI.py est de créer une interface utilisateure qui présente un menu de jeu avec un titre, un arrière-plan et les boutons "Play!", "Settings!" et "Stats!". Ainsi, chaque bouton a son propre fonctionnment :

- Le bouton "Play!" a comme but de lancer le jeu, lorsqu'il est pesé par l'utilisateur.
- Le bouton "Settings!" a comme but d'afficher un menu de paramètres du jeu où l'utilisateur peut changer le niveau de difficulté à "Easy", "Normal" ou même "Hard".
- Le bouton "Stats!" a comme but d'afficher un menu de statistiques. Ainsi, la progression de l'utilisateur est montrée dans le menu comme son nom, son niveau d'xp. Aussi, quel est le plus haut "level" que le joueur a complété avant de se faire vaincre.

## Niveaux et progression
### Niveaux
Tous les niveaux sont générés aléatoirement de manière à ce que chaque partie soient uniques.
### Progression
Une fois que vous avez tué assez d'ennemis, une porte "X" s'ouvrira "|" et vous pourrez passer au prochain niveau.
## Interactions avec le jeux
Avant le premier mouvement le joueur apparait toujours au milieu à gauche de l'écran. 
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
- Les monstres appliquent du dégat à chaque fois que le joueur fait une action s'il se retrouve dans la zone à la fin de son action.
- Attaquer fait du dégat autours du joueurs à une distance de 2 (donc ne passe pas à travers les murs comme le aura farmer)
- Déposer une bombe fait apparaitre une bombe à la position du joueur et vous avez 5 déplacement avant que la bombe explose à une distance de 3 (comme le aura farmer)
PS: les bombes détruisent les murs

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
- **Luc Desforges**
  - Classes des Acteurs: joueur et ennemis
    - Coordonnées
    - Vie, Dégat, Zone
    - Compteur de potions/bombes
  - Repertoire et Types de NPC
  - Déplacements acteurs
  - Dégat de zone
  - Interactions intermodules
  - Coordination
  - Structure générale
- **Antoine D-C**
   - Génération de niveaux
     - Labyrinthe
     - Pièges
     - Spawns
     - Coffres
     - Joueur
     - Sortie
- **Léonard Lefebvre**
  - Interactions des Acteurs: joueur et ennemis
    - Distance entre acteurs
    - Déplacements acteurs
    - AI ennemis
    - Spawns
- **Emmanuel Bissonnette**
  - Interactions des objets
    - Pièges
    - Bombes
    - Coffres
    - Sortie
      - Changement de niveau
    - Joueur
    - Ennemis
- **James Bergeron**
  - Interface visuel
    - Menus
      - Difficultés
      - Statistiques
    - Boutons
- **Marvyn Mbeugmo**
  - Progression
    - Principe XP
    - Logique de prochain niveau
    - Planification de progression en profondeur
