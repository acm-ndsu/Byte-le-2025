from game.commander_clash.character.character import Leader, GenericAttacker, GenericTank, GenericHealer, GenericTrash
from game.commander_clash.character.stats import AttackStat, DefenseStat, SpeedStat
from game.commander_clash.moves.moves import Attack, Buff, Debuff, Heal
from game.commander_clash.moves.effects import AttackEffect, BuffEffect, DebuffEffect, HealEffect
from game.commander_clash.moves.moveset import Moveset
from game.common.enums import ObjectType, CharacterType, TargetType

"""
This file is used to create the different leaders and generic characters. In this file, all attributes of a character 
(stats, movesets, etc.) will be set here.
"""


def generate_anahita() -> Leader:
    # We first make the secondary effect for readability
    # We then create the primary move and add the secondary effect to it
    nm_effect: HealEffect = HealEffect(target_type=TargetType.SELF, heal_points=15)
    nm: Attack = Attack(name='Baja Blast', target_type=TargetType.SINGLE_OPP, effect=nm_effect, damage_points=2)

    s1: Buff = Buff(name='Ice Water at 3am', target_type=TargetType.ENTIRE_TEAM, cost=2, effect=None, buff_amount=2, stat_to_affect=ObjectType.ATTACK_STAT)

    s2_effect: AttackEffect = AttackEffect(target_type=TargetType.SELF, damage_points=20)
    s2: Heal = Heal(name='Oasis', target_type=TargetType.ADJACENT_ALLIES, cost=4, effect=s2_effect, heal_points=75)

    # Then we add the finished moves into a moveset
    moves: Moveset = Moveset((nm, s1, s2))

    hp: int = 42
    atk: AttackStat = AttackStat(38)
    defense: DefenseStat = DefenseStat(30)
    spd: SpeedStat = SpeedStat(50)

    return Leader(name='Anahita', character_type=CharacterType.HEALER, health=hp, attack=atk, defense=defense, speed=spd, moveset=moves)


def generate_berry() -> Leader:
    return Leader(name='Berry', character_type=CharacterType.HEALER)


def generate_fultra() -> Leader:
    nm_effect: BuffEffect = BuffEffect(target_type=TargetType.SELF, buff_amount=1)
    nm: Attack = Attack(name='Plasma Arrow', target_type=TargetType.SINGLE_OPP, effect=nm_effect, damage_points=0)

    s1_effect: DebuffEffect = DebuffEffect(target_type=TargetType.SELF, debuff_amount=-3, stat_to_affect=ObjectType.ATTACK_STAT)
    s1: Heal = Heal(name='Overhaul', target_type=TargetType.SELF, cost=2, effect=s1_effect, heal_points=30)

    # Discuss damage_points for this one
    s2_effect: AttackEffect = AttackEffect(target_type=TargetType.ALL_OPPS, damage_points=20)
    s2: Attack = Attack(name='Lightning Rod', target_type=TargetType.SINGLE_OPP, cost=5, effect=s2_effect, damage_points=0)

    hp: int = 33
    atk: AttackStat = AttackStat(50)
    defense: DefenseStat = DefenseStat(36)
    spd: SpeedStat = SpeedStat(41)
    # Then we add the finished moves into a moveset
    moves: Moveset = Moveset((nm, s1, s2))

    return Leader(name='Fultra', character_type=CharacterType.ATTACKER, health=hp, attack=atk, defense=defense, speed=spd, moveset=moves)


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
