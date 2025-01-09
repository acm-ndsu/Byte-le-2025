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


