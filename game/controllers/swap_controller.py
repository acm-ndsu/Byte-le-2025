from game.common.player import Player
from game.common.map.game_board import GameBoard
from game.common.enums import ActionType
from game.controllers.controller import Controller
from game.common.team_manager import *


class SwapController(Controller):
    """
    `Swap Controller Notes:`

        The Swap Controller manages the swap actions the player tries to execute. Players can move up and down to swap placed.
        If the player tries to move into a space that's impassable, they don't move.

        For example, if the player attempts to move into an Occupiable Station (something the player can be on) that is
        occupied by a Wall object (something the player can't be on), the player doesn't move; that is, if the player
        tries to move into anything that can't be occupied by something, they won't move.
    """

    def __init__(self):
        super().__init__()

    def handle_actions(self, action: ActionType, client: Player, world: GameBoard) -> None:
        characters_pos: dict[Vector, Character] = world.get_characters(client.team_manager.country)
        active_character: Character = client.team_manager.get_active_character()

        pos_mod: Vector

        # Determine pos_mod based on swapping up or down
        match action:
            case ActionType.SWAP_UP:
                pos_mod = Vector(x=0, y=-1)
            case ActionType.SWAP_DOWN:
                pos_mod = Vector(x=0, y=1)
            case _:  # default case
                return

        # Set active_character's took_action to True as their turn has started
        active_character.took_action = True

        new_vector: Vector = Vector.add_vectors(active_character.position, pos_mod)

        # If character is attempting to leave the gameboard, prevent it (there is no escape)
        if new_vector not in world.get_in_bound_coords():
            return

        # Get character to swap to if there is one
        swapped_character: Character | None = characters_pos.get(new_vector)

        # First remove the acting character from the board
        # Then, if there is a swapped character, move them to the acting characters former position
        # Then finish moving the acting character to the new position
        world.remove_coordinate(active_character.position)

        if swapped_character is not None:
            world.remove_coordinate(swapped_character.position)
            swapped_character.position = active_character.position
            world.place(active_character.position, swapped_character)

        active_character.position = new_vector
        world.place(new_vector, active_character)


