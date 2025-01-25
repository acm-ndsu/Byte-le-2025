==========
Game Logic
==========

.. raw:: html

    <style> .purple {color:#A020F0; font-weight:bold; font-size:16px} </style>
    <style> .gold {color:#D4AF37; font-weight:bold; font-size:16px} </style>
    <style> .red {color:#BC0C25; font-weight:bold; font-size:16px} </style>
    <style> .blue {color:#1769BC; font-weight:bold; font-size:16px} </style>
    <style> .gold {color:#E1C564; font-weight:bold; font-size:16px} </style>
    <style> .green {color:#469B34; font-weight:bold; font-size:16px} </style>

.. role:: purple
.. role:: gold
.. role:: red
.. role:: blue
.. role:: gold
.. role:: green

The mechanics of this game are similar to many RPGs, but they are still unique in how some things are handled. Here
is how the game logic works for this game.


Priority of Actions
===================

Swapping
--------

Before any Move logic happens (anything related to Attacks, Heals, Buffs, or Debuffs), *swapping will always take
priority and happen first*. If a character on the :gold:`Uroda` team wants to swap and a character on the
:purple:`Turpis` team wants to attack, *the* :gold:`Uroda` *character would swap first* before the :purple:`Turpis`
performs a Move. If *both* characters wanted to swap, they would swap as normal.


Speed Control
-------------

If 2 characters plan on performing a Move as their action, this is when the Speed stat truly matters. When managing the
Speed of two characters, there is the possibility of *speed ties* occurring. Here are examples on how the following
situations would play out.

Example 1: Outspeed
...................

Characters taking action:

- :gold:`Uroda Attacker`
    - Speed: 40
- :purple:`Turpis Tank`
    - Speed: 30

In this example, the :gold:`Uroda Attacker` will perform a Move first. If, for example, it's an Attack that would kill
the :purple:`Turpis Tank`, the Turpis Tank would be defeated and cannot take the action it previously wanted to.


Example 2: Speed Ties
.....................

Characters taking action:

- :gold:`Uroda Attacker`
    - Speed: 40
- :purple:`Turpis Attacker`
    - Speed: 40

In this example, a speed tie is present. Say the :gold:`Uroda Attacker` and :purple:`Turpis Attacker` both want to
use an Attack and both could be defeated. In this case, both would be able to attack *and* be defeated at the
end of the turn.


Example 3: Speed Ties with Move Priorities
..........................................

Characters taking action:

- :gold:`Uroda Attacker`
    - Speed: 40
- :purple:`Turpis Healer`
    - Speed: 40

In this example, another speed tie is present. Say the :gold:`Uroda Attacker` wants to use an Attack since the
:purple:`Turpis Healer` is almost defeated, but the :purple:`Turpis Healer` wants to use a Heal. Since they have the
same speed and are using different types of Moves, the order of what happens here is determined by Move priorities.

Here are all MoveTypes and their Move priorities:

#. :green:`Heal`
#. :red:`Buff`
#. :blue:`Debuff`
#. :gold:`Attack`

This means that the :purple:`Turpis Healer` would apply it's Heal Move *first*, and then the :gold:`Uroda Attacker`
would attack *after*.


Maximum and Minimum Stat Values
===============================

Maximum Values
--------------

Stats have a maximum value they could reach to prevent absurd values and outputs from damage calculations. The
maximum values depend on the Stat.

- Attack Maximum: 99
- Defense Maximum: 75
- Speed Maximum: 99


Minimum Value
-------------

The minimum value for all stats is 1.

Move Logic Helper Methods (put me in helper.rst)
================================================

Gameboard Helper Methods (put me in helper.rst)
===============================================
