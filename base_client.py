from game.client.user_client import UserClient
from game.commander_clash.character.character import Generic, Leader
from game.commander_clash.validate_team import validate_team_selection as validate
from game.common.enums import *


class Client(UserClient):
    # Variables and info you want to save between turns go here
    def __init__(self):
        super().__init__()

    def team_name(self) -> str:
        """
        Allows the team to set a team name.
        :return: Your team name
        """
        return 'Team 1'

    def team_selection(self) -> tuple[Leader, Generic, Generic]:
        """
        Returns a tuple containing a Leader and 2 Generic characters in that order to build the user's team. If
        a character is in the wrong position (i.e., Leader at index 1 or 2), it will be replaced by a default value of
        Generic Attacker.
        """
        return validate(SelectLeader.FULTRA, SelectGeneric.GEN_ATTACKER, SelectGeneric.GEN_ATTACKER)

    # This is where your AI will decide what to do
    def take_turn(self, turn, actions, world, avatar):
        """
        This is where your AI will decide what to do.
        :param turn:        The current turn of the game.
        :param actions:     This is the actions object that you will add effort allocations or decrees to.
        :param world:       Generic world information
        """
        pass
