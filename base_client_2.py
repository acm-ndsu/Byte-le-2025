import random

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
        Returns your team name and a tuple of enums representing the characters you want for your team.
        The tuple of the team must be ordered as (Leader, Generic, Generic). If an enum is not placed in the correct
        order (e.g., (Generic, Leader, Leader)), whichever selection is incorrect will be swapped with a default value
        of Generic Attacker.
        """
        return 'Berry Defense', (SelectGeneric.GEN_TANK, SelectLeader.BERRY, SelectGeneric.GEN_TANK)

    def first_turn_init(self, team_manager: TeamManager):
        """
        This is where you can put setup for things that should happen at the beginning of the first turn. This can be
        edited as needed.
        """
        self.country = team_manager.country
        self.my_team = team_manager.team
        self.current_state = State.HEALTHY

    def get_health_percentage(self, character: Character):
        """
        Returns a float representing the health of the given character.
        :param character: The character to get the health percentage for.
        """
        return character.current_health / character.max_health

    # This is where your AI will decide what to do
    def take_turn(self, turn: int, actions: list[ActionType], world: GameBoard, team_manager: TeamManager):
        """
        This is where your AI will decide what to do.
        :param turn:         The current turn of the game.
        :param actions:      This is the actions object that you will add effort allocations or decrees to.
        :param world:        Generic world information
        :param team_manager: A class that wraps the list of Characters to control
        """
        if turn == 1:
            self.first_turn_init(team_manager)

        active_character = team_manager.get_active_character()

        # determine if the current character is healthy
        self.current_state = State.HEALTHY if self.get_health_percentage(active_character) > 50.0 else State.UNHEALTHY

        if self.current_state == State.HEALTHY:
            # if the current character from the team is healthy, use its Normal Move
            actions = [ActionType.USE_NM]
        else:
            # if unhealthy, randomly swap in a direction or attack
            actions = [random.choice([ActionType.SWAP_UP, ActionType.SWAP_DOWN, ActionType.USE_NM])]

        return actions
