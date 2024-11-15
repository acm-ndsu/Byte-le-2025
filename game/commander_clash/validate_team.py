from game.commander_clash.character.character import Generic, Character
from game.commander_clash.generation.character_generation import *
from game.common.enums import SelectLeader, SelectGeneric


def validate_team_selection(
        enums: tuple[SelectGeneric, SelectLeader, SelectGeneric]) -> list[Character]:
    """
    Checks if the given tuple has SelectLeader, SelectGeneric, SelectGeneric. If any of the characters are not the class
    they should be, it will be replaced with a Generic Attacker
    """

    gen1, leader, gen2 = [__convert_to_character(enum) for enum in enums]

    # if the leader is the same class as both generics (e.g., Tank, Tank, Tank), the leader must be replaced with trash
    # this should only be done if the leader is an actual Leader object
    if gen1.character_type == leader.character_type == gen2.character_type and isinstance(leader, Leader):
        leader = GenericTrash()

    if not isinstance(gen1, Generic):
        gen1 = GenericTrash()

    if not isinstance(gen2, Generic):
        gen2 = GenericTrash()

    if not isinstance(leader, Leader):
        leader = GenericTrash()

    # return a list of the characters in the order they would appear in the GameBoard
    return [gen1, leader, gen2]


def __convert_to_character(enum: SelectGeneric | SelectLeader):
    match enum:
        case SelectLeader.ANAHITA:
            return generate_anahita()
        case SelectLeader.BERRY:
            return generate_berry()
        case SelectLeader.FULTRA:
            return generate_fultra()
        case SelectLeader.NINLIL:
            return generate_ninlil()
        case SelectLeader.CALMUS:
            return generate_calmus()
        case SelectLeader.IRWIN:
            return generate_irwin()
        case SelectGeneric.GEN_ATTACKER:
            return generate_generic_attacker()
        case SelectGeneric.GEN_HEALER:
            return generate_generic_healer()
        case SelectGeneric.GEN_TANK:
            return generate_generic_tank()
