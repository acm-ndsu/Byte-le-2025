from game.common.player import Player
from game.common.map.game_board import GameBoard
from game.common.enums import *
from game.utils.vector import Vector
from game.controllers.controller import Controller
from game.common.team_manager import *


class MoveController(Controller):
    """
    A controller that allows for characters to use a move from their moveset. If given the correct enum,
    it will access that move and call its `use()` method to attempt to activate it.
    """

    def handle_actions(self, action: ActionType, client: Player, world: GameBoard):
        match action:
            case ActionType.USE_NA:
                na: Move =
            case ActionType.USE_S1:
                pass
            case ActionType.USE_S2:
                pass
            case ActionType.USE_S3:
                pass
            case _:
                return

