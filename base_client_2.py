"""
Wah
Nick Althoff
North Dakota State University
"""

import random
from game.utils.vector import *

from game.client.user_client import UserClient
from game.commander_clash.character.character import Character
from game.common.enums import *
from game.common.map.game_board import GameBoard
from game.common.team_manager import TeamManager


class State(Enum):
    HEALTHY = auto()
    UNHEALTHY = auto()


class Client(UserClient):
    # Variables and info you want to save between turns go here
    def __init__(self):
        super().__init__()

    def team_data(self) -> tuple[str, tuple[SelectGeneric, SelectLeader, SelectGeneric]]:
        """
        Returns your team name (to be shown on visualizer) and a tuple of enums representing the characters you
        want for your team. The tuple of the team must be ordered as (Generic, Leader, Generic). If an enum is not
        placed in the correct order (e.g., (Generic, Leader, Leader)), whichever selection is incorrect will be
        swapped with a default value of Generic Attacker.
        """
        return 'Wah', (SelectGeneric.GEN_HEALER, SelectLeader.CALMUS, SelectGeneric.GEN_HEALER)

    def first_turn_init(self, team_manager: TeamManager):
        """
        This is where you can put setup for things that should happen at the beginning of the first turn. This can be
        edited as needed.
        """
        self.country = team_manager.country_type
        self.my_team = team_manager.team
        self.current_state = State.HEALTHY

    def get_health_percentage(self, character: Character):
        """
        Returns a float representing the health of the given character.
        :param character: The character to get the health percentage for.
        """
        return float(character.current_health / character.max_health)

    # This is where your AI will decide what to do
    def take_turn(self, turn: int, actions: list[ActionType], world: GameBoard, team_manager: TeamManager):
        game_map = world.game_map

        """
        This is where your AI will decide what to do.
        :param turn:         The current turn of the game.
        :param actions:      This is the actions object that you will add effort allocations or decrees to.
        :param world:        Generic world information
        :param team_manager: A class that wraps the list of Characters to control
        """
        if turn == 1:
            self.first_turn_init(team_manager)

        # get your active character for the turn; may be None
        active_character: Character = self.get_my_active_char(team_manager, world)

        # if there is no active character for my team on this current turn, return an empty list
        if active_character is None:
            return []

        # determine if the active character is healthy
        if self.get_health_percentage(active_character) >= 0.75:
            current_state: State = State.HEALTHY
        else:
            current_state: State = State.UNHEALTHY

        # set up my own variable so I know how it works better
        enemy_leader = ""
        my_side = active_character.position.as_tuple()[0]
        if my_side == 1:
            their_side = 0
        else:
            their_side = 1
        game_world = [["", "", ""], ["", "", ""]]
        leader_y_value = 7
        for i in range(2):
            for j in range(3):
                if Vector(i, j) in game_map:
                    game_world[i][j] = game_map[Vector(i, j)].get_top()
                    if game_world[i][j].rank_type == RankType.LEADER and i == their_side:
                        enemy_leader = game_world[i][j].object_type
                    if game_world[my_side][j] != "":
                        if game_world[my_side][j].rank_type == RankType.LEADER:
                            leader_y_value = j
        # Establish threats
        priority = [0, 0, 0]
        for j in range(3):
            if game_world[their_side][j] != "":
                if game_world[their_side][j].class_type == ClassType.ATTACKER:
                    priority[j] += 2
                if game_world[their_side][j].class_type == ClassType.HEALER:
                    priority[j] += 5
                    if enemy_leader == ObjectType.BERRY and game_world[their_side][j].rank_type == RankType.GENERIC:
                        priority[j] += 5
                if game_world[their_side][j].class_type == ClassType.TANK:
                    priority[j] += 1
                if game_world[their_side][j].rank_type == RankType.LEADER:
                    priority[j] += 3
                    if game_world[their_side][j].class_type == ClassType.HEALER:
                        priority[i] -= 7
                if game_world[their_side][j].rank_type == RankType.GENERIC:
                    priority[j] += 1
        # Find highest priority
        highest_priority = 0
        highest_priority_location = 0
        for i in range(3):
            if priority[i] > highest_priority:
                highest_priority = priority[i]
                highest_priority_location = i

        actions: list[ActionType]
        leader_guy = ""
        generics = []
        for i in team_manager.team:
            if i.rank_type == RankType.LEADER:
                leader_guy = i
            else:
                generics.append(i)
        total_health = 0
        total_max_health = 0
        if leader_guy != "":
            total_health += leader_guy.current_health
            total_max_health += leader_guy.max_health
        if generics != []:
            for i in generics:
                total_health += i.current_health
                total_max_health += i.max_health

        # Do the thing
        if active_character.rank_type == RankType.GENERIC:
            if leader_guy != "" and leader_y_value != highest_priority_location:
                if leader_y_value > highest_priority_location and active_character.position.as_tuple()[
                    1] == leader_y_value - 1:
                    actions = [ActionType.SWAP_DOWN]
                elif leader_y_value < highest_priority_location and active_character.position.as_tuple()[
                    1] == leader_y_value + 1:
                    actions = [ActionType.SWAP_UP]
                else:
                    if active_character.special_points >= 3 and total_health < total_max_health * 0.85:
                        actions = [ActionType.USE_S2]
                    elif active_character.current_health < 250:
                        actions = [ActionType.USE_S1]
                    else:
                        actions = [ActionType.USE_NM]
            else:
                if active_character.special_points >= 3 and total_health < total_max_health * 0.85:
                    actions = [ActionType.USE_S2]
                elif active_character.current_health < 250 or game_world[their_side][
                    active_character.position.as_tuple()[1]] == "":
                    actions = [ActionType.USE_S1]
                else:
                    actions = [ActionType.USE_NM]

        if active_character.rank_type == RankType.LEADER:
            if (generics == [] and leader_y_value != highest_priority_location) or (
                    game_world[their_side][leader_y_value] == ""):
                if leader_y_value > highest_priority_location:
                    actions = [ActionType.SWAP_UP]
                else:
                    actions = [ActionType.SWAP_DOWN]
            else:
                if active_character.special_points >= 5 and active_character.current_health > 300 and active_character.attack.value < 99:
                    actions = [ActionType.USE_S2]
                #           elif active_character.special_points >= 3 and active_character.current_health > 200:
                #              actions = [ActionType.USE_S1]
                else:
                    actions = [ActionType.USE_NM]

        return actions

    def get_my_active_char(self, team_manager: TeamManager, world: GameBoard) -> Character | None:
        """
        Returns your active character based on which characters have already acted. If None is returned, that means
        none of your characters can act again until the turn order refreshes. This also means your team has fewer
        characters than the opponent.
        """

        active_character = team_manager.get_active_character(world.ordered_teams, world.active_pair_index)

        return active_character
