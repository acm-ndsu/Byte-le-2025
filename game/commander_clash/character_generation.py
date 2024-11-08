from game.commander_clash.character.character import Leader, GenericAttacker, GenericTank, GenericHealer, GenericTrash
from game.common.enums import ObjectType, CharacterType


"""
This file is used to create the different leaders and generic characters. In this file, all attributes of a character 
(stats, movesets, etc.) will be set here.
"""


def generate_anahita() -> Leader:
    return Leader(name='Anahita', character_type=CharacterType.HEALER)


def generate_berry() -> Leader:
    return Leader(name='Berry', character_type=CharacterType.HEALER)


def generate_fultra() -> Leader:
    return Leader(name='Fultra', character_type=CharacterType.ATTACKER)


def generate_ninlil() -> Leader:
    return Leader(name='Ninlil', character_type=CharacterType.ATTACKER)


def generate_calmus() -> Leader:
    return Leader(name='Calmus', character_type=CharacterType.TANK)


def generate_irwin() -> Leader:
    return Leader(name='Irwin', character_type=CharacterType.TANK)


def generate_generic_attacker() -> GenericAttacker:
    return GenericAttacker(name='Generic Attacker', character_type=CharacterType.ATTACKER)


def generate_generic_healer() -> GenericHealer:
    return GenericHealer(name='Generic Healer', character_type=CharacterType.HEALER)


def generate_generic_tank() -> GenericTank:
    return GenericTank(name='Generic Tank', character_type=CharacterType.TANK)


def generate_generic_trash() -> GenericTrash:
    # all default values are appropriate for this character, so no need to provide anything else
    return GenericTrash()
