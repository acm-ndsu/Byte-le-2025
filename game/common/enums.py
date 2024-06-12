from enum import Enum, auto

"""
**NOTE:** The use of the enum structure is to make is easier to execute certain tasks. It also helps with
identifying types of Objects throughout the project.

When developing the game, add any extra enums as necessary.
"""


class DebugLevel(Enum):
    NONE = auto()
    CLIENT = auto()
    CONTROLLER = auto()
    ENGINE = auto()


class ObjectType(Enum):
    NONE = auto()
    ACTION = auto()
    PLAYER = auto()
    AVATAR = auto()
    GAMEBOARD = auto()
    VECTOR = auto()
    TILE = auto()
    WALL = auto()
    ITEM = auto()
    OCCUPIABLE = auto()
    STATION = auto()
    OCCUPIABLE_STATION = auto()
    STATION_EXAMPLE = auto()
    STATION_RECEIVER_EXAMPLE = auto()
    OCCUPIABLE_STATION_EXAMPLE = auto()
    GAME_OBJECT_CONTAINER = auto()
    CHARACTER = auto()
    GENERIC_ATTACKER = auto()
    GENERIC_HEALER = auto()
    GENERIC_TANK = auto()
    LEADER = auto()


class Country(Enum):
    URODA = auto()
    TURPIS = auto()


class Draft(Enum):
    ANAHITA = auto()
    BERRY = auto()
    FULTRA = auto()
    NINLIL = auto()
    CALMUS = auto()
    IRWIN = auto()


class Place(Enum):
    LEADER = auto()
    ATTACKER = auto()
    HEALER = auto()
    TANK = auto()


class MoveType(Enum):
    MOVE = auto()
    ATTACK = auto()
    HEAL = auto()
    GUARD = auto()
    BUFF = auto()
    DEBUFF = auto()


class TargetType(Enum):
    SELF = auto()
    SINGLE_ALLY = auto()
    ALL_ALLY = auto()
    SINGLE_OPP = auto()
    ALL_OPP = auto()


class CharacterType(Enum):
    ATTACKER = auto()
    HEALER = auto()
    TANK = auto()


class ActionType(Enum):
    # NONE = auto()
    # MOVE_UP = auto()
    # MOVE_DOWN = auto()
    # MOVE_LEFT = auto()
    # MOVE_RIGHT = auto()
    USE_NA = auto()
    USE_S1 = auto()
    USE_S2 = auto()
    USE_S3 = auto()
    GUARD_SLOT_1 = auto()
    GUARD_SLOT_2 = auto()
    GUARD_SLOT_3 = auto()
    SWAP_UP = auto()
    SWAP_DOWN = auto()
