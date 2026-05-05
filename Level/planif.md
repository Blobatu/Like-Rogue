# génération des niveaux

```
à noter que ceci est plus un document de planification qu'un guide exacte du fonctionnement de mon système, beaucoup de ce qui est écrit ici est maintenant désuet
```
## tuiles
### Structure
Pour plus de simplicité, le jeu de tuiles est stocké dans un dictionnaire de dictionnaires : le premier contient les noms des tuiles, puis ces noms se décomposent en sept lignes, chacune contenant les informations relatives à cette ligne de la tuile.

Comme ceci :
```python
tileset = {
  'cross': {
    1: '##. . . . . ##',
    2: '. . . . . . . ',
    3: '. . . . . . . ',
    4: '. . . . . . . ',
    5: '. . . . . . . ',
    6: '. . . . . . . ',
    7: '##. . . . . ##',
  },
  'strgt_horz': {
    1: '##############',
    2: '. . . . . . . ',
    3: '. . . . . . . ',
    4: '. . . . . . . ',
    5: '. . . . . . . ',
    6: '. . . . . . . ',
    7: '##############',
  },
  'strgt_vert': {
    1: '##. . . . . ##',
    2: '##. . . . . ##',
    3: '##. . . . . ##',
    4: '##. . . . . ##',
    5: '##. . . . . ##',
    6: '##. . . . . ##',
    7: '##. . . . . ##',
  },
  #etc
}
```

### Lecture
On peut ensuite les lire en parcourant chaque ligne :

```python

# pour l'imprimer
def print_single_tile(tile):  # l'entrée est la tuile à imprimer
    for i in range(1, 8):   # parcourt toutes les lignes de la tuile
        print(tileset[tile][i])    # imprime chaque ligne

# si vous souhaitez l'utiliser ailleurs
def read_single_tile(tile):  # l'entrée est la tuile à imprimer
    tile_data = []          # crée une liste pour y placer les données des tuiles
    for i in range(1, 8):   # parcourt toutes les lignes de la tuile
        tile_data.append(tileset[tile][i])  # ajoute des lignes à la liste
  return tile_data          # renvoie la liste
```
### Tuiles actuellement manquantes
Au cours des tests, j'ai constaté que, dans certains cas, des tuiles spéciales seraient nécessaires, telles que :

- Aucune, elles ont toutes été ajoutées

## Plan pour la génération de niveaux
  ### Étapes pour générer un niveau
- Générer un labyrinthe sous forme de grille codée de caractères
- Placer chaque ligne dans une liste
- Transmettre la liste au traducteur (dictionnaire où caractère : type de tuile)
- envoyer la liste traduite au système de dessin
- -- une autre solution serait de faire en sorte que le générateur de niveau affiche instantanément les noms des pièces ; la faisabilité peut dépendre de la façon dont le générateur de labyrinthe est conçu --
- -- Ou mieux encore, modifier le dictionnaire du jeu de tuiles pour que les symboles servent de clés ; je me rends compte maintenant que ce serait plus simple ; la seule raison pour laquelle ils sont sous forme de mots, c'est pour que je puisse les lire et les écrire facilement, oui, faisons ça --
- dessiner le niveau en tuiles
- prendre chaque ligne du niveau et les mettre dans une liste
- envoyer la liste au dessin d'entités

cela permet au dessin d'entités de dessiner des éléments avec des données x et y (y est un élément de la liste (ligne dans le niveau) et x est le caractère de cet élément (à remplacer par le «sprite» correct))

#### ex :

``` python
def level_gen():
    # cela génère un niveau
    return level_layout

# Les données de disposition des niveaux peuvent ressembler à ceci :
# A¬A
# |LY
# L-J
# et correspondraient à un niveau tel que celui-ci :
#   ##################
#   #....#.....##....#
#   #....##....##....#
#   #....##....##....#
#   #....##..........#
#   #....########....#
#   #....########....#
#   #................#
#   ##################

# Il est ensuite ajouté à une liste
level_data = ['A¬A', '|LY', 'L-J' ]
# ce qui nous permet de tracer le niveau ligne par ligne

# Cela reviendrait à dresser la liste de tous les éléments à utiliser, comme ceci :
level_as_tiles = [['end_b', 'crnr_lb', 'end_b'], ['strgt_vert', 'crnr_rt', '3way_ltb'], ['crnr_rt', 'strgt_horz', 'crnr_lt']]

# Vous dessinez ensuite ces éléments, comme ceci :
##########################################
##. . . . . ##. . . . . . ####. . . . . ##
##. . . . . ##. . . . . . ####. . . . . ##
##. . . . . ##. . . . . . ####. . . . . ##
##. . . . . ##. . . . . . ####. . . . . ##
##. . . . . ##. . . . . . ####. . . . . ##
##. . . . . ####. . . . . ####. . . . . ##
##. . . . . ####. . . . . ####. . . . . ##
##. . . . . ####. . . . . . . . . . . . ##
##. . . . . ####. . . . . . . . . . . . ##
##. . . . . ####. . . . . . . . . . . . ##
##. . . . . ####. . . . . . . . . . . . ##
##. . . . . ####. . . . . . . . . . . . ##
##. . . . . ##################. . . . . ##
##. . . . . ##################. . . . . ##
##. . . . . . . . . . . . . . . . . . . ##
##. . . . . . . . . . . . . . . . . . . ##
##. . . . . . . . . . . . . . . . . . . ##
##. . . . . . . . . . . . . . . . . . . ##
##. . . . . . . . . . . . . . . . . . . ##
##########################################

# Ensuite, vous prenez ce niveau dessiné et vous le divisez ligne par ligne (comme pour les données du labyrinthe précédemment)
# Ces données peuvent ensuite être transmises au module de dessin/rendu des entités 
```
Remarque : j'ai constaté que, dans mon terminal, une grille de 16x7 cases est la taille maximale raisonnable pour un niveau ; au-delà, cela devient trop grand.


## dessin des entités

### Spécifications
#### Entité «unité» unique
La disposition des tuiles forme essentiellement un carré de 7x7, mais comme les personnages sont rectangulaires, cela signifie qu'ils occupent en réalité 7 lignes x 14 caractères.

Bien que la création de salles de 7x15 permettrait de centrer certains personnages sur les tuiles, cela empêcherait de rendre les tuiles "tileable" et briserait complètement l'immersion donnée par le fait que chaque niveau est un labyrinthe complet et non simplement un ensemble de carrés individuels. Nous devrions donc nous en tenir au ratio pair de 7x14. 

Cela signifie que nous pouvons lire les données du niveau 2 caractères à la fois, ce qui nous donnerait un aspect carré approprié. Ce faisant, nous pouvons dessiner efficacement des sprites plus complexes dans le niveau

Au lieu d'être un simple `` @ ``, notre joueur peut être un `` @ `` tenant son arme « dans ses mains », comme ceci pour une épée `` \@ `` ou ceci pour un arc `` (@ `` ou même un pistolet `` ¬@ ``, et c'est réversible : `` @/ ``, `` @) ``, la plupart du temps (`` ¬ `` ne l'est pas), mais vous voyez l'idée.

Nous pouvons créer des designs spéciaux pour les ennemis : au lieu d’un simple `` E ``, nous pouvons faire un serpent `` Z_ ``, un écuyer `` \i ``, un archer `` (j ``, un lancier `` -t `` ou même un sorcier `` ~A `` ; vraiment, tout est possible à ce stade.

Nous pouvons donner aux objets des formes qui seraient autrement impossibles à mettre en œuvre, comme une boîte `` [] ``, une clé `` o¬ `` ou peut-être un banc ou une clôture `` ±± ``. 


Bien sûr, on peut toujours utiliser des objets à un seul caractère, comme une roche`` o ``, de l'argent `` $ ``, une échelle `` H `` ou une pierre tombale `` ± `` (même si c'est un rogue-like, donc je ne sais pas si ça servirait à grand-chose). Certains sprites pourraient aussi simplement être élargis, comme un piège de piques`` ^^ `` ou un passage secret `` () ``

Si c'est trop difficile à mettre en œuvre, on peut toujours s'en passer, mais je trouve que ce serait vraiment cool

#### Entités spéciales «multi-unités»
Celles-ci seraient plus difficiles à mettre en œuvre, mais donneraient de bien meilleurs résultats, comme un combat contre un boss dragon :
```
  _a' /(     ,>
~~_}\ \(    (
     \(,_(,)'
      _>, _>,
                *Ce n'est pas mon design, je n'ai pas trouvé l'auteur
```
Je n'ai aucune idée de comment cela pourrait être fait simplement, ce n'est pas mon problème pour l'instant.

## Comment diable puis-je créer un générateur de labyrinthes ?
``` Python
# ces notes ne sont que ma réflexion sur la conception du système, elles ne doivent pas être prises en compte
```

d'abord, générer un niveau aléatoire, puis vérifier tuile par tuile si ces tuiles sont valides ; si elles ne le sont pas, régénérer cette tuile à partir d'une liste de tuiles valides, ajouter cette tuile générée à une liste temporaire de «tuiles générées», puis vérifier à nouveau ; si cette tuile fonctionne, continuer ; si elle enfreint toujours une règle, le régénérer tout en vérifiant les tuiles déjà générées pour s'assurer que cette option n'a pas déjà été essayée ; si toutes les tuiles valides ont été essayées, revenir en arrière d'une tuile et modifier celle-ci, répéter.

Cela semble lent, mais c'est ma méthode et ce n'est pas comme si ce processus devait tourner en permanence de toute façon