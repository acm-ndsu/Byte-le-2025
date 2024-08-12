from game.byte_2025.moves.moves import Move
from game.common.player import Player
from game.common.map.game_board import GameBoard
from game.common.enums import *
from game.utils.vector import Vector
from game.controllers.controller import Controller
from game.common.team_manager import *
from game.byte_2025.moves.move_logic import handle_move_logic


class MoveController(Controller):
    """
    A controller that allows for characters to use a move from their moveset. If given the correct enum,
    it will access that move and call its `use()` method to attempt to activate it.
    """

    def handle_actions(self, action: ActionType, client: Player, world: GameBoard) -> None:
        """
        Given the correct enum, the matching move will be selected from the current character's moveset. If enough
        special points were gained, the move will be used; otherwise, nothing will happen.
        """
        user: Character = client.team_manager.get_active_character()
        current_move: Move

        match action:
            case ActionType.USE_NA:
                current_move: Move = user.get_na()
            case ActionType.USE_S1:
                current_move: Move = user.get_s1()
            case ActionType.USE_S2:
                current_move: Move = user.get_s2()
            case ActionType.USE_S3:
                current_move: Move = user.get_s3()
            case _:
                return

        # user cannot use the move if they don't have enough special points
        if user.special_points < current_move.cost:
            return

        # get the possible targets based on the target type
        targets: list[Character] | list = self.__get_targets(user, current_move.target_type, world)

        # don't do anything if there are no available targets
        if len(targets) == 0:
            return

        # call the move_logic file's method to handle the rest of the logic
        handle_move_logic(user, targets, current_move)

    def __get_targets(self, user: Character, target_type: TargetType, world: GameBoard) -> list[Character] | list:
        """
        Helper method that determines the necessary targets for a character. Will return a list of Character objects
        or an empty list. If an empty list is returned, the character's won't perform anything during their turn.
        """

        match target_type:
            case TargetType.SELF:
                return [user]
            case TargetType.ALLY_UP:
                # get the position that is above the character
                above_pos: Vector = user.position.add_to_vector(Vector(0, -1))
                target: GameObject = world.get_character_from(above_pos)

                # check to make sure the target is actually a character and not a potential Wall
                return [target] if target is not None else []
            case TargetType.ALLY_DOWN:
                # get the position that is below the character
                below_pos: Vector = user.position.add_to_vector(Vector(0, 1))
                target: GameObject = world.get_character_from(below_pos)

                # check to make sure the target is actually a character and not a potential Wall
                return [target] if isinstance(target, Character) else []
            case TargetType.ALL_ALLIES:
                # get_characters() returns a dict; receives the characters by getting the dict's values as a list
                return list(world.get_characters(user.country_type).values())
            case TargetType.SINGLE_OPP:
                # get the position that is across the character
                above_pos: Vector = user.position.add_to_vector(Vector(1, 0))
                target: GameObject = world.get_character_from(above_pos)

                # check to make sure the target is actually a character and not a potential Wall
                return [target] if isinstance(target, Character) else []
            case TargetType.ALL_OPPS:
                # get_characters() returns a dict; receives the characters by getting the dict's values as a list
                # gets all characters opposite the user's country_type
                return list(world.get_characters(user.get_opposing_country()).values())
            case _:
                return []
