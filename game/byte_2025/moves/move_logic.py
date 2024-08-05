from game.byte_2025.character import Character
from game.byte_2025.moves.moves import Move
from game.common.enums import MoveType

"""
This is a file that will contain static methods to help perform the logic behind each type of move.
"""


def handle_move_logic(user: Character, targets: list[Character], current_move: Move):
    """
    Handles the logic for every move type. That is, damage is applied for attacks, health is increased for healing,
    and stats are modified based on the buff/debuff
    """
    match current_move.move_type:
        case MoveType.ATTACK:
            # potential warning is from type casting; ignore
            __calc_and_apply_damage(user, targets, current_move.damage_points)
        case MoveType.HEAL:
            # potential warning is from type casting; ignore
            __apply_heal_points(user, targets, current_move.heal_points)
        case MoveType.BUFF:
            # potential warning is from type casting; ignore
            __handle_stat_modification(user, targets, current_move.buff_amount)
        case MoveType.DEBUFF:
            # potential warning is from type casting; ignore
            __handle_stat_modification(user, targets, current_move.debuff_amount)
        case _:
            return

    # subtract the cost of using the move from the character's total special points
    user.special_points -= current_move.cost

    # Need to activate effect if applicable


def calculate_damage(user: Character, target: Character, damage_points: int) -> int:
    """
    Calculates the damage done by using the following formula:

        damage_points * buff/debuff modifier - target defense

    This method can be used to plan for the competition and give competitors a way to adapt to battles.
    """

    # NOTE: the formula doesn't have the modifier yet because the stat system needs to be changed; will happen soon
    return damage_points - target.defense


def __calc_and_apply_damage(user: Character, targets: list[Character], damage_points: int):
    for target in targets:
        # get the damage to be dealt
        damage_to_deal: int = calculate_damage(user, target, damage_points)

        # reduces the target's health while preventing it from going below 0 (the setter will throw an error if < 0)
        if target.current_health - damage_to_deal < 0:
            target.current_health = 0
        else:
            target.current_health -= damage_to_deal


def __apply_heal_points(user: Character, targets: list[Character], heal_amount: int) -> None:
    """
    For every target in the list of targets, apply the heal amount to their current health. If the addition
    causes the current health to become larger than the character's max health, set it to be the max health.
    """
    for target in targets:
        if target.current_health + heal_amount > target.max_health:
            target.current_health = target.max_health
        else:
            target.current_health = target.current_health + heal_amount


def __handle_stat_modification(user: Character, targets: list[Character], modifier: float) -> None:
    # Will be implemented with the updated stat system
    pass
