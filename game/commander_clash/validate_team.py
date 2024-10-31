from game.commander_clash.character.character import Generic
from game.commander_clash.character_generation import *
from game.common.enums import SelectLeader, SelectGeneric


def validate_team_selection(
        enums: tuple[SelectLeader, SelectGeneric, SelectGeneric]) -> tuple[Leader, Generic, Generic]:
    """
    Checks if the given tuple has SelectLeader, SelectGeneric, SelectGeneric. If any of the characters are not the class
    they should be, it will be replaced with a Generic Attacker
    """

    leader, gen1, gen2 = [__convert_to_character(enum) for enum in enums]

    return (leader if isinstance(leader, Leader) else generate_generic_attacker(),
            gen1 if isinstance(gen1, Generic) else generate_generic_attacker(),
            gen2 if isinstance(gen2, Generic) else generate_generic_attacker())


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
