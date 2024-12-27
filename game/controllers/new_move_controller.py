from game.commander_clash.moves.move_logic import handle_move_logic, handle_effect_logic
from game.common.map.game_board import GameBoard
from game.common.player import Player
from game.common.team_manager import *
from game.config import DEFEATED_SCORE
from game.controllers.controller import Controller

"""
NOTES FOR NEW MOVE CONTROLLER

1. After a character from the ordered team tuple executes it's move (if applicable), set its selected move to be None
2. Always check if a character in the tuple has a selected move. If not, don't perform any logic for it
3. After logic is performed on a pair, remove that pair from the list of the ordered team
4. The game board will need to check at the end of every term if the `ordered_team` list is empty. If so, reorder the teams
"""


class NewMoveController(Controller):
    """
    A controller that allows for characters to use a move from their moveset. If given the correct enum,
    it will access that move and call its `use()` method to attempt to activate it.
    """

    def handle_logic(self, clients: list[Player], world: GameBoard) -> None:
        world.order_teams()

        # if the list is empty, return as the team managers in the game board likely aren't assigned yet
        if len(world.ordered_teams) == 0:
            return

        # get the active pair for the turn, but only get character references; that is, filter None values
        active_chars: list[Character | None] = [char for char in world.ordered_teams.pop(0) if char is not None
                                                and not char.took_action]

        # sort the list so that the fastest character is listed first
        active_chars = sorted(active_chars, key=lambda character: character.speed, reverse=True)

        is_speed_tie: bool = active_chars[0].speed == active_chars[1].speed if len(active_chars) == 2 else False

        # indicate it's a speed tie in the gameboard's turn info string
        if is_speed_tie:
            world.turn_info += f'\nIt\'s a speed tie between {active_chars[0].name} and {active_chars[1].name}!\n'

        # for every character, execute the logic for their move if applicable
        for user in active_chars:
            # if the client's character died before their turn AND it is not a speed tie, continue to next iteration
            # if it is a speed tie and the character died before their turn, they can still act to simulate them
            # attacking at the same time
            if user.is_dead and not is_speed_tie:
                continue

            # move to next iteration if no move was selected
            if user.selected_move is None:
                continue

            current_move: Move = user.selected_move
            is_normal_move: bool = user.selected_move == user.get_nm()

            # if the character cannot use the desired move, continue to next iteration
            if user.special_points < current_move.cost:
                continue

            # get the possible targets based on the target type
            primary_targets: list[Character] | list = self.__get_targets(user, current_move.target_type, world)

            # don't do anything if there are no available targets
            if len(primary_targets) == 0:
                continue

            world.turn_info += f'\nStarting {user.name}\'s turn!\n'

            # call the move_logic file's method to handle the rest of the logic
            handle_move_logic(user, primary_targets, current_move, is_normal_move, world)

            defeated_characters: list[Character] = []

            # add the defeated characters to the collection
            defeated_characters += [target for target in primary_targets if target.current_health == 0]

            # a reference to the targets specifically for the secondary effect
            effect_targets: list[Character] | list = []

            # if the current move has an effect, get the targets for it and apply the same logic
            if current_move.effect is not None:
                # get the possible targets based on the effect's target type
                effect_targets: list[Character] | list = self.__get_targets(user, current_move.effect.target_type,
                                                                            world)

                handle_effect_logic(user, effect_targets, current_move.effect, world)

                # add any additional characters to defeated_characters
                defeated_characters += [target for target in effect_targets if
                                        target not in defeated_characters and target.current_health == 0]

            for char in defeated_characters:
                world.turn_info += f'\n{user.name} defeated {char.name}!\n'

            user.took_action = True

            print(f'\nCharacters in defeated_characters: {[char.name for char in defeated_characters]}\n'
                  f'Length of defeated_characters: {len(defeated_characters)}')

            # perform the logic of defeating a character(s)
            self.__defeated_char_logic(clients, user, defeated_characters)

        # update the characters that were active this turn
        for char in active_chars:
            world.replace(char.position, char)

    def __defeated_char_logic(self, clients: list[Player], user: Character,
                              defeated_characters: list[Character]) -> None:

        # don't do anything if there are no defeated characters
        if len(defeated_characters) == 0:
            return

        client_to_use: Player = Player()

        # find the client the user character belongs to
        for client in clients:
            if client.team_manager.country_type == user.country_type:
                client_to_use = client

        # for all defeated characters, set their state to 'defeated;' remove them at start of next turn
        for defeated_char in defeated_characters:
            defeated_char.is_dead = True
            defeated_char.state = 'defeated'
            client_to_use.team_manager.score += DEFEATED_SCORE

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

                return [target] if target is not None else []
            case TargetType.ALL_OPPS:
                # get_characters() returns a dict; receives the characters by getting the dict's values as a list
                # gets all characters opposite the user's country_type
                return list(world.get_characters(user.get_opposing_country()).values())
            case _:
                return []
