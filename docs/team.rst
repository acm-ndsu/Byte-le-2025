=============
Making a Team
=============

Hiring the best mercenaries will be what aids you in winning this decisive battle. How you choose your characters --
and who you choose -- matters!


Team Formation
--------------

Every team consists of *three (3) characters*. No more, and no less! Teams will consist of *one (1) Leader* and
*two (2) Generic* characters. Leaders are stronger than Generic characters, and by finding a good combination of the
three, victory is assured!

When forming a team, you do so by modifying your ``team_data()`` method. Recall that this method returns a tuple
contain 2 objects: a string literal and a nested tuple containing three enums in a specific order.

.. code-block::

    def team_data(self) -> tuple[str, tuple[SelectGeneric, SelectLeader, SelectGeneric]]:
        return str, (SelectGeneric, SelectLeader, SelectGeneric)


The string literal will represent your team name. The nested tuple will contain specific enums determining which
characters you'd like to choose. Refer to :docs:`enums` for an expansive list of all enums.


Selecting Generics
------------------

When selecting your Generic characters, you can choose between 3 options:

- Generic Attacker
- Generic Healer
- Generic Tank


The enums to select them are the following:

.. code-block::

    SelectGeneric.GEN_ATTACKER
    SelectGeneric.GEN_HEALER
    SelectGeneric.GEN_TANK


Selecting Leaders
-----------------

When selecting your Leader character, you can choose between 6 options. There are 2 leaders per ClassType:

Attackers:
    - Fultra
    - Ninlil

Healers:
    - Anahita
    - Berry

Tanks:
    - Calmus
    - Irwin


The enums to select any one of these characters are the following:

.. code-block::

    SelectLeader.FULTRA
    SelectLeader.NINLIL
    SelectLeader.ANAHITA
    SelectLeader.BERRY
    SelectLeader.CALMUS
    SelectLeader.IRWIN


Valid Team Selections
---------------------

When selecting a team, duplicate characters are allowed, but to an extent. Every team is allowed to have a *maximum of
two (2)* characters with the same ClassType. The following will provide examples of valid team selections with
characters of duplicate CharacterTypes:

.. code-block::

    (SelectGeneric.GEN_TANK, SelectLeader.CALMUS, SelectGeneric.GEN_HEALER)
    (SelectGeneric.GEN_HEALER, SelectLeader.CALMUS, SelectGeneric.GEN_TANK)
    (SelectGeneric.GEN_TANK, SelectLeader.ANAHITA, SelectGeneric.GEN_TANK)
    (SelectGeneric.GEN_TANK, SelectLeader.FULTRA, SelectGeneric.GEN_TANK)

The first and second examples show that your Leader's ClassType can be the same as *one (1)* Generic's ClassType


Malformed Character Selection
-----------------------------

If the returned tuple from ``team_data()`` is malformed, you will *not* be given all the characters requested, so it
is important to provide characters in the right order
