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
    TEAMMANAGER = auto()
    GAMEBOARD = auto()
    VECTOR = auto()
    TILE = auto()
    WALL = auto()
    OCCUPIABLE = auto()
    GAME_OBJECT_CONTAINER = auto()
    CHARACTER = auto()
    GENERIC_ATTACKER = auto()
    GENERIC_HEALER = auto()
    GENERIC_TANK = auto()
    LEADER = auto()
    MOVESET = auto()
    ABSTRACT_MOVE = auto()
    MOVE = auto()
    ATTACK = auto()
    HEAL = auto()
    GUARD = auto()
    BUFF = auto()
    DEBUFF = auto()
    EFFECT = auto()
    ATTACK_EFFECT = auto()
    HEAL_EFFECT = auto()
    GUARD_EFFECT = auto()
    BUFF_EFFECT = auto()
    DEBUFF_EFFECT = auto()


class CountryType(Enum):
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
    BUFF = auto()
    DEBUFF = auto()


class TargetType(Enum):
    SELF = auto()
    ALLY_UP = auto()
    ALLY_DOWN = auto()
    ALL_ALLIES = auto()
    SINGLE_OPP = auto()
    ALL_OPPS = auto()


class CharacterType(Enum):
    ATTACKER = auto()
    HEALER = auto()
    TANK = auto()


class RankType(Enum):
    GENERIC = auto()
    LEADER = auto()


class ActionType(Enum):
    NONE = auto()
    USE_NA = auto()
    USE_S1 = auto()
    USE_S2 = auto()
    USE_S3 = auto()
    GUARD_UP = auto()
    GUARD_DOWN = auto()
    SWAP_UP = auto()
    SWAP_DOWN = auto()
