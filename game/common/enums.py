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
    GENERIC_TRASH = auto()
    LEADER = auto()
    MOVESET = auto()
    STAT = auto()
    ATTACK_STAT = auto()
    DEFENSE_STAT = auto()
    SPEED_STAT = auto()
    MOVE = auto()
    ATTACK_MOVE = auto()
    HEAL_MOVE = auto()
    BUFF_MOVE = auto()
    DEBUFF_MOVE = auto()
    GUARD_MOVE = auto()
    EFFECT = auto()
    ATTACK_EFFECT = auto()
    HEAL_EFFECT = auto()
    BUFF_EFFECT = auto()
    DEBUFF_EFFECT = auto()


class CountryType(Enum):
    URODA = auto()
    TURPIS = auto()


class SelectLeader(Enum):
    ANAHITA = auto()
    BERRY = auto()
    FULTRA = auto()
    NINLIL = auto()
    CALMUS = auto()
    IRWIN = auto()


class SelectGeneric(Enum):
    GEN_ATTACKER = auto()
    GEN_HEALER = auto()
    GEN_TANK = auto()


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
    GUARD = auto()


class TargetType(Enum):
    SELF = auto()
    ADJACENT_ALLIES = auto()
    ENTIRE_TEAM = auto()
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
    USE_NM = auto()
    USE_S1 = auto()
    USE_S2 = auto()
    SWAP_UP = auto()
    SWAP_DOWN = auto()
