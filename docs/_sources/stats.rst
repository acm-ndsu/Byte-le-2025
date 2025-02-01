=====
Stats
=====

.. raw:: html

    <style> .gold {color:#D4AF37; font-weight:bold; font-size:16px} </style>

.. role:: gold

Every character has a unique set of Stats, including health, attack, defense, and speed.

Health
======

.. figure:: ./_static/gifs/health_bar.gif
   :width: 215
   :align: center

Health... represents how healthy a character is. What did you expect? The health will be represented by a character's
``current_health`` over their ``max_health``, such as ``current_health/max_health``.

*Please note that a character's* ``current_health`` *and* ``max_health`` *are integers.*

Stats
=====

Knowing how to manage and monitor a character's stats will be what sets your team apart from the others, so be sure
to understand them well! How to access and use a character's stats are below.

:gold:`Please note that the following stats are objects, not integers. They have properties that are integers.`

Visual Icons
------------

Each Stat is depicted by an icon on the :doc:`visualizer`.

- Sword for the Attack Stat
- Shield for the Defense Stat
- Boot with wing for the Speed Stat

If any of these icons have an *up* arrow, that means it is buffed (i.e., the Stat's value is
*greater* than its base value). If any of the icons have a *down* arrow, that means it is debuffed
(i.e., the Stat's value is *less* than its base value).


Attack Stat
-----------

.. image:: ./_static/images/stats/attack_buff.png
   :width: 90
   :align: center

.. image:: ./_static/images/stats/attack_neutral.png
   :width: 90
   :align: center

.. image:: ./_static/images/stats/attack_debuff.png
   :width: 90
   :align: center

Attack is the amount of base damage a character can deal when using an Attack Move without any modifiers.
Essentially, it is the strength of the character, reflected by an integer between 1-100 inclusive.

For example, if the attack Stat is 50, the character will attempt to deal 50 points of damage to the target.


Defense Stat
------------

.. image:: ./_static/images/stats/defense_buff.png
   :width: 90
   :align: center

.. image:: ./_static/images/stats/defense_neutral.png
   :width: 90
   :align: center

.. image:: ./_static/images/stats/defense_debuff.png
   :width: 90
   :align: center

Defense is a percentage of the amount of damage a character can prevent from taking from an Attack, represented by an
integer between 1-75 inclusive.

For example, if the defense Stat is 50, and the incoming damage is 50, the character will prevent 50% of the damage
and take 25 points of damage.

Speed Stat
----------

.. image:: ./_static/images/stats/speed_buff.png
   :width: 90
   :align: center

.. image:: ./_static/images/stats/speed_neutral.png
   :width: 90
   :align: center

.. image:: ./_static/images/stats/speed_debuff.png
   :width: 90
   :align: center

Speed is the Stat that determines the order of your team and who gets to act first each turn. It is represented by a
value between 1-100 inclusive. Visit :doc:`game_logic` for more details about turn order and how the speed Stat
affects it.

Accessing a Character's Stats
=============================

Here is how you can access any of a character's stats:

.. code-block::

    active_character.current_health
    active_character.max_health
    active_character.attack
    active_character.defense
    active_character.speed

Here is how you can access the base values (what the original Stat of the character's Stat is; this is static)
and the modified values (the value that will constantly change with Stat buffs and debuffs) of the attack,
defense, and speed stats:

Accessing the base values:

.. code-block::

    active_character.attack.base_value
    active_character.defense.base_value
    active_character.speed.base_value

Accessing the modified values:

.. code-block::

    active_character.attack.value
    active_character.defense.value
    active_character.speed.value

Comparing Stats
===============

It may be useful to compare stats to others, and you can easily do so! You can treat the attack, defense, and speed
stats like regular integers. You can also compare any Stat with any Stat (e.g., attack == speed). You can perform the
following comparisons below with any of the stats. These are just a few examples:

.. code-block::

    active_character.attack == other_character.attack
    active_character.defense == other_character.defense
    active_character.speed == other_character.speed

    active_character.attack > other_character.defense
    active_character.speed >= other_character.defense

    active_character.defense < other_character.attack
    active_character.speed <= other_character.attack

    active_character.speed != other_character.attack


Useful Methods
==============

Here are useful methods to manage stats.

Is Maxed Method
---------------

.. code-block:: python

    def is_maxed(self) -> bool:

- Returns True if the Stat used is at its maximum value (the maximum value varies depending on the Stat)

Examples:

.. code-block:: python

    attack_is_maxed: bool = active_character.attack.is_maxed()
    defense_is_maxed: bool = active_character.defense.is_maxed()
    speed_is_maxed: bool = active_character.speed.is_maxed()

Is Minimized Method
-------------------

.. code-block:: python

    def is_minimized(self) -> bool:

- Returns True if the Stat used is at its minimum value (the minimum value will always be 1, regardless of the Stat)

Examples:

.. code-block:: python

    attack_is_minimized: bool = active_character.attack.is_minimized()
    defense_is_minimized: bool = active_character.defense.is_minimized()
    speed_is_minimized: bool = active_character.speed.is_minimized()
