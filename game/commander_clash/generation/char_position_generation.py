from game.commander_clash.character.character import Leader, Generic
from game.common.team_manager import TeamManager
from game.utils.vector import Vector


def generate_character_positions(team_managers: list[TeamManager]) -> dict:
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
