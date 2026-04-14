# Level rendering
## Tileset
### structure
for simplicity, the tileset is stored in a dictionary of dicionaries, the first holds the names of the tiles, then these names all expand into seven rows, each holding the information for that line of the tile.

like this:
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

### reading
they can then be read by looping through each line:

```python

# if you want it printed
def print_single_tile(tile):  # input the tile to print
    for i in range(1, 8):   # loops through all lines of the tile
        print(tileset[tile][i])   # prints each line

# if you want to use it elsewhere
def read_single_tile(tile):  # input the tile to print
    tile_data = []          # creates a list to put the tile data in
    for i in range(1, 8):   # loops through all lines of the tile
        tile_data.append(tileset[tile][i])  # adds lines to the list
  return tile_data          # returns the list
```
### currently missing tiles
through testing, i have found that, in some cases, special tiles would be requiered, such as:

- two opposite corners (both orientations)
- a door with a wall by it's side (basically a 3-way with a corner cut off) (would taye ages due to needing mirrored versions of all 4 rotations, that's 8 tiles, it will take a while, besides, how on earth do I label them all to be clear, fast to type and unique)


## plan for level generation
  ### steps to generate a level
- generate maze as coded grid of character
- put each line in a list
- pass list into translator (dictionnary where character : tile type)
- send translated list to drawing system 
- -- alternatively, have the level generator spit out the piece's names instantly, feasability may depend on the way the maze generator is made--
- -- Or even better yet, change the tileset dictionnary to have the symbols as it's keys, I now realise that would be simpler, the only reason they're as words is so I can read and write them easily, yeah, let's do that--
- draw level in tiles
- take each line of level and put them in list
- send list to entity drawing

this allows entity drawing to draw things with x and y data (y is element of the list (line in level) and x is character in that element (to replace as correct "sprite"))

#### ex:

``` python
def level_gen():
    #this generates a level
    return level_layout

# level layout data may look something like this:
# A¬A
# |LY
# L-J
# and would correspond to a level like this:
#   ##################
#   #....#.....##....#
#   #....##....##....#
#   #....##....##....#
#   #....##..........#
#   #....########....#
#   #....########....#
#   #................#
#   ##################

# it then gets put into a list
level_data = ['A¬A', '|LY', 'L-J' ]
# which gives us a way to draw the level line by line

# this would be the same as a list of all pieces to use,like this:
level_as_tiles = [['end_b', 'crnr_lb', 'end_b'], ['strgt_vert', 'crnr_rt', '3way_ltb'], ['crnr_rt', 'strgt_horz', 'crnr_lt']]

# you then have these pieces be drawn, like this:
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

# then you take that drawn level and split it line by line (like the maze data before)
# that can then be sent off to entity drawing/rendering 
```
note: I found that, in my terminal, a 16x7 grid of tiles Is the biggest a single level could reasonnably be, otherwise it's too big.


## entity rendering

### specifications
#### single "unit" entity
the way tiles are set up is that it is basically a 7x7 square, but since characters are rectangular, it means they are in reality 7 lines X 14 characters.

while making the rooms 7x15 would allow some sharacters to be centered on the tiles, it removes the ability to make the tiles tileable and completely breaks the immersive feeling that each level is a whole maze and not simply a collection of individual squares. we should therefore stick to the even 7x14 ratio. 

What this means is we can read the level data 2 characters at a time and that would give us an appropriate square-ish look. in doing so, we can effectivly draw more complex sprites in the level

instead of our player being a simple, say ``@``, he can be a ``@`` with his held wapeon "in his hands", like this for a sword ``\@`` or this for a bow ``(@`` or even a gun ``¬@`` and it's reversible: ``@/``, ``@)``, mostly (``¬`` is not) but you get the point.

we can make special designs for enemies, instead of a simple ``E`` , we can make a snake ``Z_``, a squire ``\i``, a archer ``(j``, a spearman ``-t`` or even a wizzard ``~A``, really, anything's possible at this point.

we can make objects have shapes that would otherwise be impossible to implement, like a box ``[]``, a key ``o¬`` or maybe a bench or a fence ``±±``. 

of course, we can still use single character objects like a rock ``o``, currency ``$``, a ladder ``H`` or a gravestone ``±`` (even though it's a rogue-like so I don't know how much use it would be). Some sprites could simply be widened too, like a spike trap ``^^`` or a secret passage ``()``

If that's too hard to implement, we can always do without but that would be very cool methinks

#### special "multi-unit" entities
these ones would be harder to implement but would give much better results, like a dragon bossfight:
```
  _a' /(     ,>
~~_}\ \(    (
     \(,_(,)'
      _>, _>,
                *not my design, couldn't find author
```
I have no idea how this could be done simply, currently not my problem.