================
Characters cont.
================

.. raw:: html

    <style> .cyan {color:#00FFFF; font-weight:bold; font-size:16px} </style>

.. role:: cyan

Here are properties and methods for Character objects that will help you as you code. The
code blocks provided are examples. As long as these are called on a Character *object*,
these will work.

Properties
==========

ObjectType
----------

Return the ObjectType of the Character. The ObjectType enum is used to better identify what an
object is. Refer to :doc:`enums` for the full lists of enums provided.

.. code-block::

    object_type: ObjectType = active_character.object_type

Name
----

Returns the name of the Character object.

.. code-block:: python

    character_name: str = active_character.name

ClassType
---------

Returns the ClassType enum of the character. Will either be ``ClassType.LEADER`` or
``ClassType.GENERIC``.

.. code-block::

    class_type: ClassType = active_character.class_type

Current Health
--------------

Returns an int showing how much health the character currently has.

.. code-block::

    current_health: int = active_character.current_health

Max Health
----------

Returns an int showing the max health a character can have.

.. code-block::

    max_health: int = active_character.max_health

Stats
-----

The following will return a Character's Attack, Defense, and Speed Stat object
respectively.

.. code-block::

    attack_stat: AttackStat = active_character.attack
    defense_stat: DefenseStat = active_character.defense
    speed_stat: SpeedStat = active_character.speed

Refer to :doc:`stats` for more info.

Special Points
--------------

Returns an int representing the amount of :cyan:`Special Points` a Character has. Remember that
this amount *cannot* exceed 5.

.. code-block::

    sp: int = active_character.special_points

Moveset
-------

Returns a Moveset object that contains all a Character's Moves (i.e., Normal Move, Special 1, and Special 2).

.. code-block::

    moveset: Moveset = active_character.moveset

Position
--------

Returns a Vector object that represent a Character's coordinates. Every Vector object is stored in the ``(x, y)``
format. Refer to :doc:`gameboard` for the methods the Vector class has.

.. code-block::

    position: Vector = active_character.position

CountryType
-----------

Return a CountryType enum representing which country the Character is affiliated with.

.. code-block::

    country: CountryType = active_character.country_type

Is Dead
-------

Returns a boolean value. The value will be True if the Character's current_health is 0.

.. code-block::

    is_dead: bool = active_character.is_dead

Methods
=======

Get NM
------

A method that will return a Character's Normal Move from their Moveset.

.. code-block::

    nm: Move = active_character.get_nm()

Get S1
------

A method that will return a Character's Special 1 from their Moveset.

.. code-block::

    s1: Move = active_character.get_s1()

Get S2
------

A method that will return a Character's Special 2 from their Moveset.

.. code-block::

    s2: Move = active_character.get_s2()
