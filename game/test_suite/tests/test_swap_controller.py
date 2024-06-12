import unittest

from game.common.map.game_board import GameBoard
from game.controllers.movement_controller import MovementController
from game.common.map.wall import Wall
from game.utils.vector import Vector
from game.common.player import Player
from game.common.action import ActionType
from game.common.team_manager import TeamManager
from game.common.game_object import GameObject


class TestSwapController(unittest.TestCase):
    """
    `Test Movement Controller if Wall Notes:`

        This class tests the Movement Controller *specifically* for when there are walls -- or other impassable
        objects -- near the Avatar.
    """

    def setUp(self) -> None:
        # TEST SWAP CONTROLLER WHEN IMPLEMENTED

        self.movement_controller = MovementController()
        self.game_board = GameBoard(0, Vector(2, 3), None, False)

        # test movements up, down, left and right by starting with default 3,3 then know if it changes from there \/
        # self.client = Player(None, None, [], self.avatar)
        # self.game_board.generate_map()

    # test move up
    def test_swap_up(self) -> None:
        pass

    # test move down
    def test_swap_down(self) -> None:
        pass

    def test_swap_up_fail(self) -> None:
        pass

    def test_swap_down_fail(self) -> None:
        pass