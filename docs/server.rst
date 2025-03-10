==========
The Server
==========

.. raw:: html

    <style> .gold {color:#E1C564; font-weight:bold; font-size:16px} </style>
    <style> .red {color:#BC0C25; font-weight:bold; font-size:16px} </style>

.. role:: gold
.. role:: red

Here are some notes to consider about the server to aid you in the competition.


Registering
===========

To register your team, type

.. code-block::

    python launcher.pyz client -register

into the terminal. Follow the prompts to enter your team name, select your university, and select if you are an alumni.

After registering, you will receive a new file called ``vID`` in your root folder. :red:`DO NOT SHARE THIS.`
This is unique to your team and allows you to submit your clients and view specific team information.

Client Commands
===============

:gold:`NOTE`: As commands are listed, some will have two versions to perform the same task. The first command will be
typed in its entirety, and the second command will be a shortened version for ease of use.

:gold:`Only ONE line needs to be typed into the terminal, NOT both.`


Submitting Code
---------------

To submit your client code, type one of the following into the terminal:

.. code-block::

    python launcher.pyz client -submit
    python launcher.pyz c -submit


After successfully registering your team, you are able to submit your client code. At least one client must be
submitted before the end of the competition to be eligible to win. You can either submit ``base_client.py`` or
``base_client_2.py``. The command will prompt you to submit ``base_client.py`` first. If you say 'no,' it will then
prompt you to submit ``base_client_2.py``.

Once uploaded to the server, your bot will run against other submitted bots to determine placing. You can submit as
many times as you'd like during the duration of the competition, but do not excessively upload please.


Leaderboard
-----------

To view the leaderboard, type one of the following in the terminal:

.. code-block::

    python launcher.pyz client leaderboard
    python launcher.pyz c l

These will return the leaderboard for all eligible contestants. By default, alumni are not included. To include
alumni, type one of the following:

.. code-block::

    python launcher.pyz client leaderboard -include_alumni
    python launcher.pyz c l -include_alumni

If you want to see previous leaderboards from the competition, you may type one of the following by providing a
leaderboard's id:

.. code-block::

    python launcher.pyz client leaderboard -leaderboard_id <leaderboard_id>
    python launcher.pyz c l -leaderboard_id <leaderboard_id>


Stats
-----

To view your stats for the latest submission, type one of the following:

.. code-block::

    python launcher.pyz client stats
    python launcher.pyz c s

Your stats will continue to change until all games are completed.

If you desire to see all of your submissions, type

.. code-block::

    python launcher.pyz client stats -get_submissions
    python launcher.pyz c s -get_submissions

to receive all your submission ids. These ids can be used in some of the commands listed below.

To receive code from a previous submission, have a submission id ready and type

.. code-block::

    python launcher.pyz client stats -get_code_for_submission <submission_id>
    python launcher.pyz c s -get_code_for_submission <submission_id>

to receive the code file from the given submission.


Extra Help
==========

For extra help on these commands, you can type ``-h`` after any of these commands to have the help message appear.
For example:

.. code-block::

    python launcher.pyz client -h
    python launcher.pyz c -h

or

.. code-block::

    python launcher.pyz client leaderboard -h
    python launcher.pyz c l -h

will show you the help descriptions of all client and leaderboard commands respectively.

Code Time-Outs
==============

Every team is allowed a maximum of 0.1 seconds for their code to execute. If your code takes longer than this
allotted time, the code will not be executed. This is to ensure the competition runs smoothly and pushes
competitors to write efficient code. Good luck, and think hard!
