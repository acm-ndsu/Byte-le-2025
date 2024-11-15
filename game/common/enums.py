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
    NONE = 1
    ACTION = 2
    PLAYER = 3
    TEAMMANAGER = 4
    GAMEBOARD = 5
    VECTOR = 6
    TILE = 7
    WALL = 8
    OCCUPIABLE = 9
    GAME_OBJECT_CONTAINER = 10
    CHARACTER = 11
    GENERIC_ATTACKER = 12
    GENERIC_HEALER = 13
    GENERIC_TANK = 14
    GENERIC_TRASH = 15
    LEADER = 16
    MOVESET = 17
    STAT = 18
    ATTACK_STAT = 19
    DEFENSE_STAT = 20
    SPEED_STAT = 21
    MOVE = 22
    ATTACK_MOVE = 23
    HEAL_MOVE = 24
    BUFF_MOVE = 25
    DEBUFF_MOVE = 26
    GUARD_MOVE = 27
    EFFECT = 28
    ATTACK_EFFECT = 29
    HEAL_EFFECT = 30
    BUFF_EFFECT = 31
    DEBUFF_EFFECT = 32


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
