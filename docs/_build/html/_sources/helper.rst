=================================
Helper Methods, Code, & Debugging
=================================

This page contains useful methods and other code that may be useful to help you during your development.

Move Logic Helper Methods
=========================

To help with potential calculations, methods are provided for you to calculate how a Move might affect a character.
To use these methods, ensure the following import statement is in your ``base_client`` file:

.. code-block:: python

    from game.commander_clash.moves.move_logic import *

Calculate Damage Method
-----------------------

Calculates the damage done by using the following formula:

``ceiling((user's attack value + current move's damage value) * (1 - target's defense value / 100))``

.. code-block:: python

    def calculate_damage(user, target, current_move) -> int:
        if isinstance(current_move, AttackEffect):
            return current_move.damage_points

        damage: int = math.ceil((user.attack.value + current_move.damage_points) * (1 - target.defense.value / 100))

        return MINIMUM_DAMAGE if damage < MINIMUM_DAMAGE else damage

- ``user``: A character object that will be using the ``current_move``. Refer to all characters in :doc:`characters`
- ``target``: A character object that's the intended target for the ``current_move``
- ``current_move``: Either an Attack Move or AttackEffect object
    - The Attack Move will incorporate its ``damage_points`` into the damage formula
    - The AttackEffect will return its damage_points without further calculations
- Returns an int representing the damage that would be dealt to the ``target`` if the ``user`` used the ``current_move``

Calculate Healing Method
------------------------

Calculates the healing done to the target by determining the smallest amount of healing possible. The numbers
compared are the heal_points and the difference between the target's max health and current health.

.. code-block:: python

    def calculate_healing(target, current_move) -> int:
        return min(current_move.heal_points, target.max_health - target.current_health)

- ``target``: A character object that will be affected by the ``current_move``
- ``current_move``: Either a Heal Move or HealEffect object
    - Both the Heal Move and HealEffect will incorporate their ``heal_points`` without any extra conditions
- Returns an int representing how much the ``current_move`` would heal the ``target``

Calculate Stat Modification Method
----------------------------------

Calculates how a stat will change when the current_move's buff or debuff amount is applied to it.

.. code-block::

    def calculate_stat_modification(target, current_move) -> int:
        stat_to_affect: Stat = __get_stat_object_to_affect(target, current_move)

        final_value: int = stat_to_affect.value + current_move.buff_amount if isinstance(current_move, AbstractBuff) else stat_to_affect.value + current_move.debuff_amount

        return final_value

- ``target``: A character object that will be affected by the ``current_move``
- ``current_move``: Either a Buff/Debuff Move or BuffEffect/DebuffEffect object
    - A Buff Move or BuffEffect object will *increase* the target's stat to affect
    - A Debuff Move or DebuffEffect object will *decrease* the target's stat to affect
- Returns an int representing the final value of the target's stat to affect if the modification would be applied

Debugging
=========

To help you in debugging, here are a few tools to help you.

The Visualizer
--------------

Of course, the visualizer will be one of the best tools to use for debugging. You will see what your characters
are doing easily, and the active character for each turn is also marked by a "!" next to their headshot.

Printing Turn Info
------------------

To help provide information for what happened every turn without using the JSON files, every turn will be
printed in your terminal. Every turn will start with "Starting turn <turn number>!" and will provide detailed
descriptions of everything. This can be useful when paired with the visualizer!

The Logs
--------

Lastly, whenever you generate and run a game, your ``logs`` folder will be created. This folder contains a
``.json`` file for every turn and stores the information that happened for that turn. If you know how to read
the format, this can also be helpful for looking in-depth at everything despite it's lower level analysis.
