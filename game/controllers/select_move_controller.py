from game.commander_clash.character.character import Character
from game.commander_clash.moves.moves import Move
from game.common.enums import ActionType
from game.common.map.game_board import GameBoard
from game.common.player import Player
from game.controllers.controller import Controller


class SelectMoveController(Controller):
    """
    A controller that sets the `selected_move` variable for a client's active character.
    """

    def handle_actions(self, action: ActionType, client: Player, world: GameBoard) -> None:
        """
        Given the correct ActionType enum, the client's active character's `selected_move` variable will be set. This
        will be used in another controller that will execute a move's logic.
        """

        user: Character = client.team_manager.get_active_character()

        current_move: Move

        match action:
            case ActionType.USE_NM:
                user.selected_move = user.get_nm()
            case ActionType.USE_S1:
                user.selected_move = user.get_s1()
            case ActionType.USE_S2:
                user.selected_move = user.get_s2()
            case _:
                return

        # set the client's version of the character to have the same selected move
        client.team_manager.get_active_character().selected_move = user.selected_move
