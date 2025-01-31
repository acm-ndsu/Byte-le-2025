=============
The Gameboard
=============

.. raw:: html

    <style> .purple {color:#A020F0; font-weight:bold; font-size:16px} </style>
    <style> .gold {color:#D4AF37; font-weight:bold; font-size:16px} </style>

.. role:: purple
.. role:: gold

Layout
======

The map is a 3x2 grid. On the map, :gold:`Uroda` will *always* be on the left, and :purple:`Turpis` will
*always* be on the right. Characters will be displayed on their country's respective side.

:gold:`NOTE: Two characters cannot be on the same spot (i.e., overlap). They will either swap spaces
or not be present at all on the board.`

.. figure:: ./_static/images/game_map.png

    Six characters displayed on a 3x2 grid.

Structure
=========

The game map is structured as a dictionary object, not a 2D array. This simplifies accessing coordinates and
objects on the map!

Every key-value pair in the dictionary will be a Vector object and a GameObjectContainer.

To access the game map from the given GameBoard object in your ``base_client`` file, do the following:

.. code-block:: python

    game_map = world.game_map


Vector Class
------------

Vector objects are what represent coordinates. They also come with different methods to simplify common functions.

Add To Vector Method
....................

Adds a given Vector objects coordinates to the Vector object being used and returns a new
Vector object.

.. code-block:: python

    def add_to_vector(self, other_vector) -> Vector:
        return Vector(self.x + other_vector.x, self.y + other_vector.y)

- ``other_vector``: A different Vector to be added with to create a new Vector
- Returns a new Vector object with the summed coordinates

Add X Y Method
..............

Similar to the ``add_to_vector()`` method, this will take two ints ``x`` and ``y`` as parameters,
add them to the Vector object being used, and return a new Vector with the summed coordiantes.

.. code-block:: python

    def add_x_y(self, x, y) -> Vector:
        return self.add_to_vector(Vector(x, y))

- ``x``: An int representing the x coordinate
- ``y``: An int representing the y coordinate
- Returns a new Vector object with the summed coordinates

Add X Method
............

Takes an int representing the x coordinate, adds it to the Vector object being used, and returns a new Vector
with the summed coordinates.

.. code-block:: python

    def add_x(self, x: int) -> Vector:
        return self.add_to_vector(Vector(x))

- ``x``: An int representing the x coordinate
- Returns a new Vector object with the summed coordinates

Add Y Method
............

Takes an int representing the x coordinate, adds it to the Vector object being used, and returns a new Vector
with the summed coordinates.

.. code-block:: python

    def add_y(self, y) -> Vector:
        return self.add_to_vector(Vector(y=y))

- ``y``: An int representing the y coordinate
- Returns a new Vector object with the summed coordinates

As Tuple Method
...............

Returns the Vector objects coordinates as a tuple object.

.. code-block:: python

    def as_tuple(self) -> Tuple[int, int]:
        return self.x, self.y
        
GameObjectContainer Class
------------------------- 

This wrapper class allows for objects to be stored and managed more easily. You will not need to worry about any 
methods in this class as they've been implemented in the GameBoard class to make life easier for you. These methods 
will be listed in the next section.

Gameboard
=========

The Gameboard stores the information for all the characters and their locations. Here are methods that will help
access the characters to analyze their states. Since the logic for these methods are heavier, 
they will not be displayed.

Get Top Method
--------------

Returns the object at the top of the given coordinate's GameObjectContainer

.. code-block:: python

    def get_top(self, coords) -> GameObject | None
    
- ``coords``: A Vector object representing the coordinate to access
- Returns a GameObject (superclass of a Character object) or None if the coordinate was not in the game map dictionary.

Is Valid Coords Method
----------------------

Takes a Vector object and evaluates if the coordinates are within the bounds of the game 
map.

.. code-block:: python

    def is_valid_coords(self, coords: Vector) -> bool
    
- ``coords``: A Vector object representing the coordinate to access
- Returns True if the given coordinates are within the bounds of the game map's size.
    - Examples for a 3x2 map:
        - world.is_valid_coords(Vector(0, 0) -> True
        - world.is_valid_coords(Vector(3, 0)) -> False
        - world.is_valid_coords(Vector(0, 4)) -> False

Get Characters Method
---------------------

Uses a CountryType enum as a parameter and returns a dictionary object
with Vector: Character key-value pairings. All characters returned would be from the given
country's team. If None is given instead of an enum, *all* characters from *both* teams will be
returned.

.. code-block:: python

    def get_characters(self, country: CountryType | None = None) -> dict[Vector, Character]

- ``country``: A CountryType enum representing the country's team to access
- Returns a dictionary of Vector objects and the character found at that coordinate. If None is given as a parameter,
  all characters on the game map will be returned instead.

Get Character From Method
-------------------------

Using the given Vector object, the character at that coordinate will be returned. None is returned if the coordinate
can't be found or if no character is at the coordinate.

.. code-block:: python

    def get_character_from(self, coords: Vector) -> Character | None:

- ``coords``: A Vector object representing the coordinate to access
- Returns a character or None if the given coordinate wasn't found or if no character was at the coordinate.

Get In Bound Coords Method
--------------------------

Returns a list of Vector objects representing all valid coordinates possible for the game map's size.

.. code-block:: python

    def get_in_bound_coords(self) -> list[Vector]

- Returns a list of Vector objects
