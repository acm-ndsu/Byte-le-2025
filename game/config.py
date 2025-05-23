import os

from game.common.enums import *

"""
This file is important for configuring settings for the project. All parameters in this file have comments to explain 
what they do already. Refer to this file to clear any confusion, and make any changes as necessary.
"""

# Runtime settings / Restrictions --------------------------------------------------------------------------------------
# The engine requires these to operate
MAX_TICKS = 350                                     # max number of ticks the server will run regardless of game state
TQDM_BAR_FORMAT = "Game running at {rate_fmt} "     # how TQDM displays the bar
TQDM_UNITS = " turns"                               # units TQDM takes in the bar

MAX_SECONDS_PER_TURN = 0.1                          # max number of basic operations clients have for their turns

MAX_NUMBER_OF_ACTIONS_PER_TURN = 1                  # max number of actions per turn is currently set to 1

MIN_CLIENTS_START = None                            # minimum number of clients required to start running the game; should be None when SET_NUMBER_OF_CLIENTS is used
MAX_CLIENTS_START = None                            # maximum number of clients required to start running the game; should be None when SET_NUMBER_OF_CLIENTS is used
SET_NUMBER_OF_CLIENTS_START = 2                     # required number of clients to start running the game; should be None when MIN_CLIENTS or MAX_CLIENTS are used
CLIENT_KEYWORD = "client"                           # string required to be in the name of every client file, not found otherwise
CLIENT_DIRECTORY = "./"                             # location where client code will be found

MIN_CLIENTS_CONTINUE = None                         # minimum number of clients required to continue running the game; should be None when SET_NUMBER_OF_CLIENTS is used
MAX_CLIENTS_CONTINUE = None                         # maximum number of clients required to continue running the game; should be None when SET_NUMBER_OF_CLIENTS is used
SET_NUMBER_OF_CLIENTS_CONTINUE = 2                  # required number of clients to continue running the game; should be None when MIN_CLIENTS or MAX_CLIENTS are used

ALLOWED_MODULES = ["game.client.user_client",       # modules that clients are specifically allowed to access
                   "game.common.enums",
                   "game.common.map.game_board",
                   "game.common.map.tile",
                   "game.common.map.wall",
                   "game.common.map.game_board",
                   "game.common.team_manager",
                   "game.commander_clash.character.character",
                   "game.commander_clash.character.stats",
                   "game.commander_clash.moves.effects",
                   "game.commander_clash.moves.moves",
                   "game.commander_clash.moves.move_logic",
                   "game.commander_clash.moves.moveset",
                   "game.commander_clash.moves.move_logic",
                   "game.utils.vector",
                   "typing",
                   "numpy",
                   "scipy",
                   "pandas",
                   "itertools",
                   "functools",
                   "random",
                   "heapq",
                   "sympy",
                   "math",
                   ]

RESULTS_FILE_NAME = "results.json"                                  # Name and extension of results file
RESULTS_DIR = os.path.join(os.getcwd(), "logs")                     # Location of the results file
RESULTS_FILE = os.path.join(RESULTS_DIR, RESULTS_FILE_NAME)         # Results directory combined with file name

LOGS_FILE_NAME = 'turn_logs.json'
LOGS_DIR = os.path.join(os.getcwd(), "logs")                        # Directory for game log files
LOGS_FILE = os.path.join(LOGS_DIR, LOGS_FILE_NAME)

GAME_MAP_FILE_NAME = "game_map.json"                                # Name and extension of game file that holds generated world
GAME_MAP_DIR = os.path.join(os.getcwd(), "logs")                    # Location of game map file
GAME_MAP_FILE = os.path.join(GAME_MAP_DIR, GAME_MAP_FILE_NAME)      # Filepath for game map file


class Debug:                    # Keeps track of the current debug level of the game
    level = DebugLevel.NONE

# Other Settings Here --------------------------------------------------------------------------------------------------

HEALTH_MODIFIER = 10                                                # The modfier to increase a character's health

STAT_MINIMUM = 1                                                    # The lowest number a stat can reach

ATTACK_MAXIMUM = 100                                                # The highest the Attack stat can reach
DEFENSE_MAXIMUM = 75                                                # The highest the Defense stat can reach
SPEED_MAXIMUM = 100                                                 # The highest the Speed stat can reach

SPECIAL_POINT_LIMIT = 5                                             # The highest amount of Special Points attainable

MINIMUM_DAMAGE = 1                                                  # Base damage to be dealt to prevent negative ints

DEFEATED_BONUS = 100                                                # The points to award for each defeated character
DIFFERENTIAL_BONUS = 150                                            # The points to award for each alive character on either team
WIN_BONUS = 250                                                     # The points to award for completely defeating the opposing team


GENERIC_TRASH_NAME = 'Missing Character'                            # A name used for Generic Trash to convey a proper message to the players
