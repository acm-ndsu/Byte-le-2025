import math

from game.byte_2025.character.character import Character, GenericTank, Leader
from game.byte_2025.character.stats import Stat
from game.byte_2025.moves.moves import *
from game.common.enums import MoveType


def handle_move_logic(user: Character, targets: list[Character], current_move: Move, is_normal_attack: bool) -> None:
    """
    Handles the logic for every move type. That is, damage is applied for attacks, health is increased for healing,
    and stats are modified based on the buff/debuff
    """

    match current_move.move_type:
        case MoveType.ATTACK:
            current_move: Attack
            __calc_and_apply_damage(user, targets, current_move)
        case MoveType.HEAL:
            current_move: Heal
            __apply_heal_points(targets, current_move)
        case MoveType.BUFF:
            current_move: Buff
            __handle_stat_modification(targets, current_move)
        case MoveType.DEBUFF:
            current_move: Debuff
            __handle_stat_modification(targets, current_move)
        case MoveType.GUARD:
            current_move: Guard
            user: GenericTank | Leader
            __assign_guardian(user, targets)
        case _:
            return

    if is_normal_attack:
        # add 1 to the user's special points if using a normal attack
        user.special_points += 1

    # subtract the cost of using the move from the character's total special points
    user.special_points -= current_move.cost


def handle_effect_logic(user: Character, targets: list[Character], current_effect: Effect) -> None:
    match current_effect.move_type:
        case MoveType.ATTACK:
            current_effect: AttackEffect
            __calc_and_apply_damage(user, targets, current_effect)
        case MoveType.HEAL:
            current_effect: HealEffect
            __apply_heal_points(targets, current_effect)
        case MoveType.BUFF:
            current_effect: BuffEffect
            __handle_stat_modification(targets, current_effect)
        case MoveType.DEBUFF:
            current_effect: DebuffEffect
            __handle_stat_modification(targets, current_effect)
        case _:
            return


def calculate_damage(user: Character, target: Character, current_move: AbstractAttack) -> int:
    """
    Calculates the damage done by using the following formula:

        ceiling(damage_points * attack stat modifier) - target's defense stat

    The ceiling function is applied to the (damage_points * attack stat modifier) part of the formula to do the
    most damage possible.

    This method can be used to plan for the competition and give competitors a way to adapt to battles.
    """

    attack_stage: int = user.attack.stage

    return math.ceil(current_move.damage_points * user.attack.calculate_modifier(attack_stage)) - target.defense.value


def calculate_healing(target: Character, current_move: AbstractHeal) -> int:
    """
    Calculates the healing done to the target by determining the smallest amount of healing possible. The numbers
    compared are the heal_points and the difference between the target's max health and current health.

    Example:
        Target health: 10/10
        heal_points: 5

        If target health = 4/10, return 5 since healing more than 5 isn't possible
        If target health = 5/10, return 5
        If target health = 6/10, return 4 since healing 5 isn't possible
    """

    return min(current_move.heal_points, target.max_health - target.current_health)


def calculate_modifier_effect(target: Character, current_move: AbstractBuff | AbstractDebuff) -> int:
    """
    Calculates and returns the potential value of the stat if the given Buff/Debuff is used.
    """

    stat = __get_stat_object_to_affect(target, current_move)
    modifier: float = stat.calculate_modifier(current_move.stage_amount)

    # return the calculation done without applying it to the character
    return math.ceil(stat.base_value * modifier)


def __calc_and_apply_damage(user: Character, targets: list[Character], current_move: AbstractAttack):
    """
    Calculates the damage to deal for every target and applies it to the target's health.
    """

    for target in targets:
        # get the damage to be dealt
        damage_to_deal: int = calculate_damage(user, target, current_move)

        # reduces the target's health while preventing it from going below 0 (the setter will throw an error if < 0)
        if target.current_health - damage_to_deal < 0:
            target.current_health = 0
        else:
            target.current_health -= damage_to_deal


def __apply_heal_points(targets: list[Character], current_move: AbstractHeal) -> None:
    """
    For every target in the list of targets, apply the heal amount to their current health. If the addition
    causes the current health to become larger than the character's max health, set it to be the max health.
    """

    # cannot reassign heal_amount, so make a new int that will store the new value calculated
    adjusted_healing_amount: int

    for target in targets:
        # calculate the healing amount
        adjusted_healing_amount = calculate_healing(target, current_move)

        target.current_health = target.current_health + adjusted_healing_amount


def __handle_stat_modification(targets: list[Character], current_move: AbstractBuff | AbstractDebuff) -> None:
    """
    Gets the modification needed from the current_move and applies it to every target's corresponding stat.
    """

    stat: Stat

    for target in targets:
        stat = __get_stat_object_to_affect(target, current_move)
        stat.apply_modifier(current_move.stage_amount)


def __get_stat_object_to_affect(target: Character, current_move: AbstractBuff | AbstractDebuff) -> Stat:
    """
    A helper method that returns the Stat object to buff/debuff based on the current_move's stat_to_affect.
    """

    match current_move.stat_to_affect:
        case ObjectType.ATTACK_STAT:
            return target.attack
        case ObjectType.DEFENSE_STAT:
            return target.defense
        case ObjectType.SPEED_STAT:
            return target.speed


def __assign_guardian(guardian: GenericTank | Leader, targets: list[Character]):
    """
    A helper method that assigns the given tank character to the given targets.
    """

    # This checks to see if the character using the guard move is a tank or a tank leader, and if not, it returns.
    if guardian.character_type is not CharacterType.TANK:
        return

    for target in targets:
        if target.guardian is not None:
            continue

        target.guardian = guardian
