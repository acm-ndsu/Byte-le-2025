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

        if user is None:
            print(f'No active character found for client {client.team_name}.\nCurrent world `ordered_teams` list: '
                  f'{[(obj1.name if obj1 is not None else None, 
                       obj2.name if obj2 is not None else None) 
                      for obj1, obj2 in world.ordered_teams]}')

            input('\n\nEnter > ')

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

        # give the reference in the ordered_teams on the gameboard the same selected move
        for pair in world.ordered_teams:
            for char in pair:
                if char is not None and char.name == user.name:
                    char.selected_move = user.selected_move
                    break
