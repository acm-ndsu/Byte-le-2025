=======
Scoring
=======

.. raw:: html

    <style> .red {color:#BC0C25; font-weight:bold; font-size:16px} </style>
    <style> .blue {color:#1769BC; font-weight:bold; font-size:16px} </style>
    <style> .gold {color:#E1C564; font-weight:bold; font-size:16px} </style>

.. role:: red
.. role:: blue
.. role:: gold


In order to win the war, points are what matter most! Here is how points will be totaled. The country with the most
points will secure victory!

========================== =============== =============================================================================
Method                     Points          Description
========================== =============== =============================================================================
:red:`Defeated Character`  100             These will be awarded for every character you defeat on the opposing side.
                                           Go get 'em!
:blue:`Differential Bonus` 150             These points will be awarded for every character that is alive on your team
                                           by the end of a game. Try to win without losing valuable fighters!
:gold:`Win`                200             Your country :gold:`won` the war - congratulations! Now the land can know
                                           peace.
========================== =============== =============================================================================

Point Table
-----------

Here's a table showing how the score will change depending on how many characters are alive on the winning team.

==================================== ===== ===== =====
Characters Lost on Winning Team      0     1     2
==================================== ===== ===== =====
:gold:`Winner`                       950   800   650
:red:`Loser`                         0     100   200
==================================== ===== ===== =====


Final Score Formula
-------------------

``# of defeated characters (100)`` + ``# of alive characters on your team (150)`` + ``winner's bonus``
