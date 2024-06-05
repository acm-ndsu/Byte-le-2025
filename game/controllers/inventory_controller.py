from game.common.enums import *
from game.common.avatar import Avatar
from game.common.player import Player
from game.controllers.controller import Controller
from game.common.map.game_board import GameBoard


class InventoryController(Controller):
    """
    `Interact Controller Notes:`

        The Inventory Controller is how player's can manage and interact with their inventory. When given the enum to
        select an item from a slot in the inventory, that will then become the held item.

        If an enum is passed in that is not within the range of the inventory size, an error will be thrown.
    """

    def __init__(self):
        super().__init__()

    def handle_actions(self, action: ActionType, client: Player, world: GameBoard) -> None:
        # If a larger inventory is created, create more enums and add them here as needed
        avatar: Avatar = client.avatar

        # If there are more than 10 slots in the inventory, change "ActionType.SELECT_SLOT_9"
        # This checks if the given action isn't one of the select slot enums
        if action.value < ActionType.SELECT_SLOT_0.value or action.value > ActionType.SELECT_SLOT_9.value:
            return

        index: int = action.value - ActionType.SELECT_SLOT_0.value

        try:
            avatar.held_item = avatar.inventory[index]
        except IndexError:
            raise IndexError(f'The given action type, {action.name}, is not within bounds of the given inventory of '
                             f'size {len(avatar.inventory)}. Select an ActionType enum that will be within the '
                             f'inventory\'s bounds.')
