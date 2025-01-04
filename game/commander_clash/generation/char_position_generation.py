import json

from game.commander_clash.character.character import Leader, Generic, Character
from game.common.enums import CountryType, RankType, CharacterType, ObjectType
from game.common.team_manager import TeamManager
from game.config import GAME_MAP_FILE
from game.utils.helpers import write_json_file
from game.utils.vector import Vector


def generate_locations_dict(team_managers: list[TeamManager]) -> dict:
    locations: dict = dict()

    for team_manager in team_managers:
        x_pos: int = team_manager.country_type.value - 1

        # get the leader and generic instances from the team manager
        leader: Leader = next(char for char in team_manager.team if isinstance(char, Leader))
        generics: list[Generic] = [gen for gen in team_manager.team if isinstance(gen, Generic)]

        # add the characters in the following order: Generic, Leader, Generic
        locations.update({Vector(x_pos, 0): [generics[0]]})
        locations.update({Vector(x_pos, 1): [leader]})
        locations.update({Vector(x_pos, 2): [generics[1]]})

        # add the country name to the character's name if it's a generic to help with identification
        for character in team_manager.team:
            if isinstance(character, Generic):
                country_name: str = team_manager.country_type.name
                country_name = country_name[0].upper() + country_name[1:].lower()
                character.name = f'{country_name} {character.name}'

    return locations


def update_character_info(team_managers: list[TeamManager]):
    """
    Gives all characters in the team managers their country affiliation and positions.
    """
    with open(GAME_MAP_FILE) as json_file:
        world = json.load(json_file)

        for team_manager in team_managers:
            x_pos: int = team_manager.country_type.value - 1

            for y_pos, character in enumerate(team_manager.team):
                # update the character position and country type
                character.position = Vector(x_pos, y_pos)
                character.country_type = team_manager.country_type

                # assign the generic characters their specific object types for the visualizer
                __assign_generic_object_type(character)

            if team_manager.country_type == CountryType.URODA:
                world['game_board']['uroda_team_manager'] = team_manager.to_json()
            else:
                world['game_board']['turpis_team_manager'] = team_manager.to_json()

        write_json_file(world, GAME_MAP_FILE)


def __assign_generic_object_type(char: Character):
    """
    Gives a Generic character their ObjectType based on their country and their CharacterType.
    """
    if char.rank_type == RankType.GENERIC:
        country_name: str = char.country_type.name.lower()

        # Mapping of (country_name, character_type) to ObjectType
        object_type_map = {
            ('uroda', CharacterType.ATTACKER): ObjectType.URODA_GENERIC_ATTACKER,
            ('uroda', CharacterType.HEALER): ObjectType.URODA_GENERIC_HEALER,
            ('uroda', CharacterType.TANK): ObjectType.URODA_GENERIC_TANK,
            ('turpis', CharacterType.ATTACKER): ObjectType.TURPIS_GENERIC_ATTACKER,
            ('turpis', CharacterType.HEALER): ObjectType.TURPIS_GENERIC_HEALER,
            ('turpis', CharacterType.TANK): ObjectType.TURPIS_GENERIC_TANK
        }

        # Assign the appropriate ObjectType based on the map
        char.object_type = object_type_map.get((country_name, char.character_type))
