========================
Taking Character Actions
========================

To control your characters, you do so by using :doc:`enums`.


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
