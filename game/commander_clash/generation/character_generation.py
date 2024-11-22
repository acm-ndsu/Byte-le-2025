from game.commander_clash.character.character import Leader, GenericAttacker, GenericTank, GenericHealer, GenericTrash
from game.commander_clash.character.stats import AttackStat, DefenseStat, SpeedStat
from game.commander_clash.moves.effects import AttackEffect, BuffEffect, DebuffEffect, HealEffect
from game.commander_clash.moves.moves import Attack, Buff, Debuff, Heal
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

    s1: Buff = Buff(name='Ice Water at 3am', target_type=TargetType.ENTIRE_TEAM, cost=2, effect=None, buff_amount=2,
                    stat_to_affect=ObjectType.ATTACK_STAT)

    s2_effect: AttackEffect = AttackEffect(target_type=TargetType.SELF, damage_points=20)
    s2: Heal = Heal(name='Oasis', target_type=TargetType.ADJACENT_ALLIES, cost=4, effect=s2_effect, heal_points=75)

    # Then we add the finished moves into a moveset
    moves: Moveset = Moveset((nm, s1, s2))

    hp: int = 42
    atk: AttackStat = AttackStat(38)
    defense: DefenseStat = DefenseStat(30)
    spd: SpeedStat = SpeedStat(50)

    return Leader(name='Anahita', character_type=CharacterType.HEALER, health=hp, attack=atk, defense=defense,
                  speed=spd, moveset=moves)


def generate_berry() -> Leader:
    # We first make the secondary effect for readability
    # We then create the primary move and add the secondary effect to it
    nm_effect: HealEffect = HealEffect(target_type=TargetType.SELF, heal_points=6)
    nm: Heal = Heal(name='Healing Potion', target_type=TargetType.ENTIRE_TEAM, effect=nm_effect, heal_points=6)

    s1: Debuff = Debuff(name='Debuff Potion', target_type=TargetType.SINGLE_OPP, cost=1, effect=None, debuff_amount=-2,
                        stat_to_affect=ObjectType.ATTACK_STAT)

    s2_effect: BuffEffect = BuffEffect(target_type=TargetType.SELF, buff_amount=5)
    s2: Buff = Buff(name='Buffing Potion', target_type=TargetType.ADJACENT_ALLIES,
                    cost=4, effect=s2_effect, buff_amount=5)

    # Then we add the finished moves into a moveset
    moves: Moveset = Moveset((nm, s1, s2))

    hp: int = 40
    atk: AttackStat = AttackStat(1)
    defense: DefenseStat = DefenseStat(50)
    spd: SpeedStat = SpeedStat(69)
    return Leader(name='Berry', character_type=CharacterType.HEALER, health=hp, attack=atk, defense=defense, speed=spd,
                  moveset=moves)


def generate_fultra() -> Leader:
    nm_effect: BuffEffect = BuffEffect(target_type=TargetType.SELF, buff_amount=1)
    nm: Attack = Attack(name='Plasma Arrow', target_type=TargetType.SINGLE_OPP, effect=nm_effect, damage_points=0)

    s1_effect: DebuffEffect = DebuffEffect(target_type=TargetType.SELF, debuff_amount=-3,
                                           stat_to_affect=ObjectType.ATTACK_STAT)
    s1: Heal = Heal(name='Overhaul', target_type=TargetType.SELF, cost=2, effect=s1_effect, heal_points=30)

    # !!!!!!!!!!!!!!!!!!!!!!!!!!Discuss damage_points for this one!!!!!!!!!!!!!!!!!!!!!!!
    s2_effect: AttackEffect = AttackEffect(target_type=TargetType.ALL_OPPS, damage_points=20)
    s2: Attack = Attack(name='Lightning Rod', target_type=TargetType.SINGLE_OPP, cost=5, effect=s2_effect,
                        damage_points=0)

    hp: int = 33
    atk: AttackStat = AttackStat(50)
    defense: DefenseStat = DefenseStat(36)
    spd: SpeedStat = SpeedStat(41)

    moves: Moveset = Moveset((nm, s1, s2))

    return Leader(name='Fultra', character_type=CharacterType.ATTACKER, health=hp, attack=atk, defense=defense,
                  speed=spd, moveset=moves)


def generate_ninlil() -> Leader:
    nm: Attack = Attack(name='Little Angy', target_type=TargetType.SINGLE_OPP, effect=None, damage_points=5)

    s1_effect: DebuffEffect = DebuffEffect(target_type=TargetType.SELF, debuff_amount=-3,
                                           stat_to_affect=ObjectType.SPEED_STAT)
    s1: Attack = Attack(name='Smol Rage', target_type=TargetType.SINGLE_OPP, cost=2, effect=s1_effect, damage_points=10)

    s2_effect: DebuffEffect = DebuffEffect(target_type=TargetType.SELF, debuff_amount=-5,
                                           stat_to_affect=ObjectType.SPEED_STAT)
    s2: Attack = Attack(name='Tiny Titan', target_type=TargetType.SINGLE_OPP, cost=5, effect=s2_effect, damage_points=15)

    hp: int = 46
    atk: AttackStat = AttackStat(47)
    defense: DefenseStat = DefenseStat(37)
    spd: SpeedStat = SpeedStat(30)

    moves: Moveset = Moveset((nm, s1, s2))

    return Leader(name='Ninlil', character_type=CharacterType.ATTACKER, health=hp, attack=atk, defense=defense,
                  speed=spd, moveset=moves)


def generate_calmus() -> Leader:
    nm: Attack = Attack(name='Flare Slash', target_type=TargetType.SINGLE_OPP, effect=None, damage_points=5)

    s1_effect = AttackEffect(target_type=TargetType.SELF, damage_points=10)
    s1: Buff = Buff(name='Flash Boost', target_type=TargetType.SELF, cost=3, effect=None, buff_amount=4,
                    stat_to_affect=ObjectType.ATTACK_STAT)

    s2_effect: AttackEffect = AttackEffect(target_type=TargetType.SELF, damage_points=35)
    s2: Buff = Buff(name='Berserk', target_type=TargetType.ENTIRE_TEAM, cost=5, effect=s2_effect, buff_amount=15,
                    stat_to_affect=ObjectType.ATTACK_STAT)

    # Then we add the finished moves into a moveset
    moves: Moveset = Moveset((nm, s1, s2))

    hp: int = 60
    atk: AttackStat = AttackStat(45)
    defense: DefenseStat = DefenseStat(35)
    spd: SpeedStat = SpeedStat(20)

    return Leader(name='Calmus', character_type=CharacterType.TANK, health=hp, attack=atk, defense=defense,
                  speed=spd, moveset=moves)


def generate_irwin() -> Leader:
    nm_effect = BuffEffect(target_type=TargetType.SELF, buff_amount=1, stat_to_affect=ObjectType.DEFENSE_STAT)
    nm: Attack = Attack(name='Impale', target_type=TargetType.SINGLE_OPP, damage_points=1, effect=nm_effect)

    s1_effect = DebuffEffect(target_type=TargetType.SINGLE_OPP, debuff_amount=3, stat_to_affect=ObjectType.DEFENSE_STAT)
    s1: Attack = Attack(name='Stab Repeatedly', target_type=TargetType.SINGLE_OPP, cost=3, effect=s1_effect)

    s2_effect = DebuffEffect(target_type=TargetType.SELF, debuff_amount=15, stat_to_affect=ObjectType.DEFENSE_STAT)
    s2: Attack = Attack(name='Ultra Stab', target_type=TargetType.SINGLE_OPP, cost=5, damage_points=10,
                        effect=s2_effect)

    hp: int = 55
    atk: AttackStat = AttackStat(30)
    defense: DefenseStat = DefenseStat(50)
    spd: SpeedStat = SpeedStat(25)

    moves: Moveset = Moveset((nm, s1, s2))

    return Leader(name='Irwin', character_type=CharacterType.TANK, health=hp, attack=atk, defense=defense,
                  speed=spd, moveset=moves)


def generate_generic_attacker() -> GenericAttacker:
    # We first make the secondary effect for readability
    # We then create the primary move and add the secondary effect to it
    nm: Attack = Attack(name='Poke', target_type=TargetType.SINGLE_OPP, damage_points=5)

    s1: Attack = Attack(name='Stab', target_type=TargetType.SINGLE_OPP, cost=1, damage_points=10)

    # Discuss damage_points for this one
    s2_effect: DebuffEffect = DebuffEffect(target_type=TargetType.SELF, debuff_amount=-1,
                                           stat_to_affect=ObjectType.SPEED_STAT)
    s2: Attack = Attack(name='Slash', target_type=TargetType.ALL_OPPS, cost=2, effect=s2_effect,
                        damage_points=7)

    hp: int = 40
    atk: AttackStat = AttackStat(45)
    defense: DefenseStat = DefenseStat(30)
    spd: SpeedStat = SpeedStat(35)
    # Then we add the finished moves into a moveset
    moves: Moveset = Moveset((nm, s1, s2))
    return GenericAttacker(name='Generic Attacker', character_type=CharacterType.ATTACKER, health=hp, attack=atk,
                           defense=defense,
                           speed=spd, moveset=moves)


def generate_generic_healer() -> GenericHealer:
    nm: Attack = Attack(name='Kick', target_type=TargetType.SINGLE_OPP, damage_points=1)

    s1: Heal = Heal(name='First Aid', target_type=TargetType.SELF, cost=0, heal_points=10)

    # Discuss damage_points for this one
    s2: Heal = Heal(name='Heal', target_type=TargetType.ENTIRE_TEAM, cost=3,
                    heal_points=25)

    hp: int = 39
    atk: AttackStat = AttackStat(34)
    defense: DefenseStat = DefenseStat(36)
    spd: SpeedStat = SpeedStat(41)
    # Then we add the finished moves into a moveset
    moves: Moveset = Moveset((nm, s1, s2))
    return GenericHealer(name='Generic Healer', character_type=CharacterType.HEALER, health=hp, attack=atk,
                         defense=defense,
                         speed=spd, moveset=moves)


def generate_generic_tank() -> GenericTank:
    nm: Attack = Attack(name='Slap', target_type=TargetType.SINGLE_OPP, damage_points=2)

    s1: Attack = Attack(name='Slam', target_type=TargetType.ALL_OPPS, cost=2, damage_points=4)

    # Discuss damage_points for this one
    s2_effect: DebuffEffect = DebuffEffect(target_type=TargetType.SINGLE_OPP, debuff_amount=-1,
                                           stat_to_affect=ObjectType.SPEED_STAT)
    s2: Attack = Attack(name='Stomp', target_type=TargetType.SINGLE_OPP, cost=3, effect=s2_effect,
                        damage_points=0)

    hp: int = 55
    atk: AttackStat = AttackStat(30)
    defense: DefenseStat = DefenseStat(50)
    spd: SpeedStat = SpeedStat(36)
    # Then we add the finished moves into a moveset
    moves: Moveset = Moveset((nm, s1, s2))
    return GenericTank(name='Generic Tank', character_type=CharacterType.TANK, health=hp, attack=atk, defense=defense,
                       speed=spd, moveset=moves)


def generate_generic_trash() -> GenericTrash:
    # all default values are appropriate for this character, so no need to provide anything else
    return GenericTrash()
