========================
Taking Character Actions
========================

To control your characters, you do so by using :doc:`enums`.


Actions List
============

As you code, your ``take_turn()`` method *needs* to return a list. That list is currently named ``actions``. This
list needs to consist of only ActionType enums.

Even though a list is being returned, *only the first enum in the list will be executed*. Please be mindful of this
as you code! (This is simply due to the engine. Could it have been changed? ... yes, but we aren't paid for this. :D)


Active Character
================

As you code, the character that is taking action is not determined by you, but by the environment. Every character will
take their turn in a cyclical manner based on their Speed stat.

In your ``take_turn()`` method, your ``active_character`` for the turn is already provided for you, but here's how it
changes so you understand the game cycle.

Gameboard's Ordered Team
------------------------

The gameboard stores a list of tuples which is called ``ordered_teams``.

.. code-block:: python

    ordered_teams: list[tuple[Character | None, Character | None]] = world.ordered_teams

Each tuple is ordered by a Uroda character in the first index, and a Turpis character in the second index (this
ordering does not interfere with character taking their turns if one is faster than the other, so don't worry about
that). Either index can be a None value *if* that respective team has less characters than the other.

To know which pairing would be taking their turn for either team, you can use the gameboard's ``active_pair_index``
variable to access the correct pair:

.. code-block:: python

    active_pair_for_turn: tuple[Character | None, Character | None] = world.ordered_teams[world.active_pair_index]

With this, you can see what character from the opposing team will also be taking action their action
*if applicable*. Remember - if a value in the tuple is None, that means that team cannot have a character taking an
action that turn. Again, the order of the tuples are (Uroda character,  Turpis character).

How the Cycle Continues
-----------------------

As stated previously, your ``active_character`` rotates cyclically based on your team manager's ``team`` list.

.. code-block:: python

    alive_team: list[Character] = team_manager.team

The ``active_pair_index`` for the gameboard will *always reset to the first index after reaching the last index
of the* ``ordered_teams`` *list*. Here is the order of events for how the process works:

#. Let the active pair take their turn
#. Increment the ``active_pair_index``
    - Repeat until the last pair of ``ordered_teams`` executes their turn
#. Remove any dead characters from the gameboard and team managers
#. Reorganize ``ordered_teams`` based on every alive character's speed stat
#. Set the ``active_pair_index`` to 0
#. Go back to step 1

Normal Move
===========

The Normal Move is the base move for every character. This Move
is used to fill your Special Point meter, which is used for Moves
called Specials. *Every Normal Move costs zero special points*.

To use a character's Normal Move, set your ``actions`` list to be:

.. code-block::

    actions = [ActionType.USE_NM]

Your ``actions`` list will be what your code
returns at the end of the ``take_turn()`` method, and the order will determine
which character -- in order of speed priority -- does the listed action.

Special Move 1
==============

The Special Move 1 is a low special point Move, and costs for this Move
vary by Move.

To use a character's Special Move 1, set your ``actions`` list to be:

.. code-block::

    actions = [ActionType.USE_S1]

Special Move 2
==============

The Special Move 2 is a high special point Move and costs for this Move
vary by Move.

To use a character's Special Move 2, set your ``actions`` list to be:

.. code-block::

    actions = [ActionType.USE_S2]

Swapping
========

A character can also Swap, allowing a character to switch places
with an adjacent character *on their team*, but it will not allow you to move out of
bounds. If a match up is not going well for a character on your team, this
enables you to tactically move to a better position! The Swapping :doc:`enums`
are listed below.

Swap Up
-------

A character can use Swap Up to Swap with a character above them.

To use a character's Swap Up, set your ``actions`` list to be:

.. code-block::

    actions = [ActionType.SWAP_UP]

Swap Down
---------

A character can use Swap Down to Swap with a character below them.

To use a character's Swap Down, set your ``actions`` list to be:

.. code-block::

    actions = [ActionType.SWAP_DOWN]

Note
----

Note that a character is still able to swap to a space even if an ally isn't positioned there. That is, *your characters
will always be able to swap as long as it is not out of bounds*.
