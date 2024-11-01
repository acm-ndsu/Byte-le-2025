from game.commander_clash.character.character import Leader, GenericAttacker, GenericTank, GenericHealer, GenericTrash

"""
This file is used to create the different leaders and generic characters. In this file, all attributes of a character 
(stats, movesets, etc.) will be set here.
"""


def generate_anahita() -> Leader:
    return Leader(name='Anahita')


def generate_berry() -> Leader:
    return Leader(name='Berry')


def generate_fultra() -> Leader:
    return Leader(name='Fultra')


def generate_ninlil() -> Leader:
    return Leader(name='Ninlil')


def generate_calmus() -> Leader:
    return Leader(name='Calmus')


def generate_irwin() -> Leader:
    return Leader(name='Irwin')


def generate_generic_attacker() -> GenericAttacker:
    return GenericAttacker(name='Generic Attacker')


def generate_generic_healer() -> GenericHealer:
    return GenericHealer(name='Generic Healer')


def generate_generic_tank() -> GenericTank:
    return GenericTank(name='Generic Tank')


def generate_generic_trash() -> GenericTrash:
    # all default values are appropriate for this character, so no need to provide anything else
    return GenericTrash()
