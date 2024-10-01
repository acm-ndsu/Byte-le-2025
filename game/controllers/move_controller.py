from game.common.player import Player
from game.common.map.game_board import GameBoard
from game.controllers.controller import Controller
from game.common.team_manager import *
from game.commander_clash.moves.move_logic import handle_move_logic, handle_effect_logic


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

        # Set user's took_action to True as they have started their action
        user.took_action = True

        current_move: Move

        # a bool to be passed into the handle_logic method
        is_normal_attack: bool = False

        match action:
            case ActionType.USE_NM:
                current_move: Move = user.get_nm()
                is_normal_attack = True
            case ActionType.USE_S1:
                current_move: Move = user.get_s1()
            case ActionType.USE_S2:
                current_move: Move = user.get_s2()
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
        handle_move_logic(user, targets, current_move, is_normal_attack)

        # a collection of the defeated characters is created
        defeated_characters: list[Character] = [target for target in targets if target.is_defeated()]

        # if the current move has an effect, get the targets for it and apply the same logic
        if current_move.effect is not None:
            # get the possible targets based on the effect's target type
            targets: list[Character] | list = self.__get_targets(user, current_move.effect.target_type, world)

            handle_effect_logic(user, targets, current_move.effect)

            # add any additional characters to defeated_characters
            defeated_characters += [target for target in targets if target.is_defeated()]

        # for all defeated characters, set their state to 'defeated;' remove them at start of next turn
        for defeated_char in defeated_characters:
            defeated_char.state = 'defeated'

    def __get_targets(self, user: Character, target_type: TargetType, world: GameBoard) -> list[Character] | list:
        """
        Helper method that determines the necessary targets for a character. Will return a list of Character objects
        or an empty list. If an empty list is returned, the character's won't perform anything during their turn.
        """

        match target_type:
            case TargetType.SELF:
                return [user]
            case TargetType.ADJACENT_ALLIES:
                result: list = []

                # get the position that is above the character
                above_pos: Vector = user.position.add_to_vector(Vector(0, -1))
                below_pos: Vector = user.position.add_to_vector(Vector(0, 1))

                # get the actual targets
                above_target: GameObject = world.get_character_from(above_pos)
                below_target: GameObject = world.get_character_from(below_pos)

                # if neither character is None, add them to the list
                if above_target is not None:
                    result.append(above_target)

                if below_target is not None:
                    result.append(below_target)

                return result
            case TargetType.ENTIRE_TEAM:
                # get_characters() returns a dict; receives the characters by getting the dict's values as a list
                return list(world.get_characters(user.country_type).values())
            case TargetType.SINGLE_OPP:

                # adjusts the vector value based on who is attacking, so it attacks across from the user
                adjustment_vector: Vector = Vector(1, 0) if user.country_type is CountryType.URODA else Vector(-1, 0)

                # get the position that is across the character
                across_pos: Vector = user.position.add_to_vector(adjustment_vector)
                target: Character | None = world.get_character_from(across_pos)

                # if the target doesn't exist then return an empty list
                if target is None:
                    return []

                # if the target.guardian doesn't exist, then it returns the target, otherwise it returns the guardian
                # return [target.guardian] if target.guardian is not None else [target]
                if target.guardian is None:
                    return [target]

                guardian: list[Character] = [target.guardian]
                target.guardian = None
                return guardian
            case TargetType.ALL_OPPS:
                # get_characters() returns a dict; receives the characters by getting the dict's values as a list
                # gets all characters opposite the user's country_type
                return list(world.get_characters(user.get_opposing_country()).values())
            case _:
                return []
