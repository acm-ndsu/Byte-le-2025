import json

from game.commander_clash.character.character import Leader, Generic
from game.common.enums import CountryType
from game.common.team_manager import TeamManager
from game.config import GAME_MAP_FILE
from game.utils.helpers import write_json_file
from game.utils.vector import Vector


def generate_locations_dict(team_managers: list[TeamManager]) -> dict:
    locations: dict = dict()

    for team_manager in team_managers:
        x_pos: int = team_manager.country.value - 1

        # get the leader and generic instances from the team manager
        leader: Leader = next(char for char in team_manager.team if isinstance(char, Leader))
        generics: list[Generic] = [gen for gen in team_manager.team if isinstance(gen, Generic)]

        # add the characters in the following order: Generic, Leader, Generic
        locations.update({Vector(x_pos, 0): [generics[0]]})
        locations.update({Vector(x_pos, 1): [leader]})
        locations.update({Vector(x_pos, 2): [generics[1]]})

    return locations


def assign_and_write_positions(team_managers: list[TeamManager]):
    with open(GAME_MAP_FILE) as json_file:
        world = json.load(json_file)

        for team_manager in team_managers:
            x_pos: int = team_manager.country.value - 1

            for y_pos, character in enumerate(team_manager.team):
                character.position = Vector(x_pos, y_pos)

            if team_manager.country == CountryType.URODA:
                world['game_board']['uroda_team_manager'] = team_manager.to_json()
            else:
                world['game_board']['turpis_team_manager'] = team_manager.to_json()

        write_json_file(world, GAME_MAP_FILE)
