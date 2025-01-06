import json

from game.commander_clash.character.character import Leader, Generic
from game.common.enums import CountryType, RankType, ObjectType
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

        # add the country name to the character's name to help with identification
        for character in team_manager.team:
            country_name: str = team_manager.country_type.name
            country_name = country_name[0].upper() + country_name[1:].lower()
            character.name = f'{country_name} {character.name}'

            # assign the specific ObjectType for the generic character
            if character.rank_type == RankType.GENERIC:
                match character.name:
                    case 'Uroda Attacker' | 'Uroda Attacker 2':
                        character.object_type = ObjectType.URODA_GENERIC_ATTACKER
                    case 'Uroda Healer' | 'Uroda Healer 2':
                        character.object_type = ObjectType.URODA_GENERIC_HEALER
                    case 'Uroda Tank' | 'Uroda Tank 2':
                        character.object_type = ObjectType.URODA_GENERIC_TANK
                    case 'Turpis Attacker' | 'Turpis Attacker 2':
                        character.object_type = ObjectType.TURPIS_GENERIC_ATTACKER
                    case 'Turpis Healer' | 'Turpis Healer 2':
                        character.object_type = ObjectType.TURPIS_GENERIC_HEALER
                    case 'Turpis Tank' | 'Turpis Tank 2':
                        character.object_type = ObjectType.TURPIS_GENERIC_TANK

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

            if team_manager.country_type == CountryType.URODA:
                world['game_board']['uroda_team_manager'] = team_manager.to_json()
            else:
                world['game_board']['turpis_team_manager'] = team_manager.to_json()

        write_json_file(world, GAME_MAP_FILE)
