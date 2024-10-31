from game.client.user_client import UserClient
from game.common.enums import *


class Client(UserClient):
    # Variables and info you want to save between turns go here
    def __init__(self):
        super().__init__()

    def team_data(self) -> tuple[str, tuple[SelectLeader, SelectGeneric, SelectGeneric]]:
        """
        Returns your team name and a tuple of enums representing the characters you want for your team.
        The tuple of the team must be ordered as (Leader, Generic, Generic). If an enum is not placed in the correct
        order (e.g., (Generic, Leader, Leader)), whichever selection is incorrect will be swapped with a default value
        of Generic Attacker.
        """
        return 'Team 1', (SelectLeader.ANAHITA, SelectGeneric.GEN_ATTACKER, SelectGeneric.GEN_ATTACKER)

    # This is where your AI will decide what to do
    def take_turn(self, turn, actions, world, team_manager):
        """
        This is where your AI will decide what to do.
        :param turn:         The current turn of the game.
        :param actions:      This is the actions object that you will add effort allocations or decrees to.
        :param world:        Generic world information
        :param team_manager: A class that wraps the list of Characters to control
        """
        pass
