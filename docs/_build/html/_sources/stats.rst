=====
Stats
=====

Every character has a unique set of stats, including attack, defense, and speed.

Attack
------

Attack is the amount of base damage a character can deal when using an Attack move. Essentially, it is the strength of
the character, reflected by an integer between 0 and 100.

For example, if the attack stat is 50, the character will attempt to deal 50 points of damage to the target.

Defense
-------

Defense is a percentage of the amount of damage a character can prevent from taking from an Attack, represented by an
integer between 0 - 100.

For example, if the defense stat is 50, and the incoming damage is 50, the character will prevent 50% of the damage
and take 25 points of damage.

Speed
-----

Speed is the stat that determines the turn order of your team and who gets to act first each turn. Visit
:doc:`Game Logic` for more details about turn order and how the speed stat affects it.
