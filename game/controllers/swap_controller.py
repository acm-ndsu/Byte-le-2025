import game.common.map.game_board
from game.common.player import Player
from game.common.map.game_board import GameBoard
from game.common.enums import *
from game.utils.vector import Vector
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

    def handle_actions(self, action: ActionType, client: Player, world: GameBoard):
        characters_pos: dict[Vector, Character] = world.get_characters(client.team_manager.country)
        character: Character = client.team_manager.get_active_character()
        pos_mod: Vector
        # Determine pos_mod based on swapping up or down
        match action:
            case ActionType.SWAP_UP:
                pos_mod = Vector(x=0, y=-1)
            case ActionType.SWAP_DOWN:
                pos_mod = Vector(x=0, y=1)
            case _:  # default case
                return
        new_vector: Vector = Vector.add_vectors(character.position, pos_mod)
        # If character is attempting to leave the gameboard, prevent it (there is no escape)
        if new_vector not in world.get_positions():
            return
        # Get character to swap to if there is one
        swapped_character: Character | None = characters_pos.get(new_vector)
        # Swap characters First remove the acting character from the board, then, if there is a swapped character,
        # move them, then finish moving the acting character
        world.remove_coordinate(character.position)
        if swapped_character is not None:
            world.remove_coordinate(swapped_character.position)
            swapped_character.position = character.position
            world.place(character.position, swapped_character)
        character.position = new_vector
        world.place(new_vector, character)


