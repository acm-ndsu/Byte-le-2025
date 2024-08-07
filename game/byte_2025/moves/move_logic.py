from game.byte_2025.character.character import Character
from game.byte_2025.moves.moves import *
from game.common.enums import MoveType

"""
This is a file that will contain static methods to help perform the logic behind each type of move.
"""


def handle_move_logic(user: Character, targets: list[Character], current_move: Move) -> None:
    """
    Handles the logic for every move type. That is, damage is applied for attacks, health is increased for healing,
    and stats are modified based on the buff/debuff
    """

    # user cannot use the move if they don't have enough special points
    if user.special_points < current_move.cost:
        return

    match current_move.move_type:
        case MoveType.ATTACK:
            current_move: Attack
            __calc_and_apply_damage(targets, current_move)
        case MoveType.HEAL:
            current_move: Heal
            __apply_heal_points(targets, current_move)
        case MoveType.BUFF:
            current_move: Buff
            __handle_stat_modification(targets, current_move)
        case MoveType.DEBUFF:
            current_move: Debuff
            __handle_stat_modification(targets, current_move)
        case _:
            return

    # subtract the cost of using the move from the character's total special points
    user.special_points -= current_move.cost

    # Need to activate effect if applicable
    # effect activation will be implemented on the Stat branch since I'll be able to fully implement it


def calculate_damage(target: Character, current_move: Attack) -> int:
    """
    Calculates the damage done by using the following formula:

        damage_points * buff/debuff modifier - target defense

    This method can be used to plan for the competition and give competitors a way to adapt to battles.
    """

    # NOTE: the formula doesn't have the modifier yet because the stat system needs to be changed; will happen soon
    return current_move.damage_points - target.defense


def calculate_healing(target: Character, current_move: Heal) -> int:
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


def calculate_modifier_effect(target: Character, modifier: float) -> int:
    """
    Calculates and returns the value of the stat if the modifier can be applied.
    """

    # will be implemented in the Stat branch
    pass


def __calc_and_apply_damage(targets: list[Character], current_move: Attack):
    """
    Calculates the damage to deal for every target and applies it to the target's health.
    """

    for target in targets:
        # get the damage to be dealt
        damage_to_deal: int = calculate_damage(target, current_move)

        # reduces the target's health while preventing it from going below 0 (the setter will throw an error if < 0)
        if target.current_health - damage_to_deal < 0:
            target.current_health = 0
        else:
            target.current_health -= damage_to_deal


def __apply_heal_points(targets: list[Character], current_move: Heal) -> None:
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

        # if target.current_health + heal_amount > target.max_health:
        #     target.current_health = target.max_health
        # else:
        #     target.current_health = target.current_health + heal_amount


def __handle_stat_modification(targets: list[Character], current_move: Buff | Debuff) -> None:
    # Will be implemented with the updated stat system
    pass
