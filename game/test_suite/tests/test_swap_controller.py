import unittest

from game.byte_2025.character import Character
from game.common.map.game_board import GameBoard
from game.controllers.swap_controller import SwapController
from game.utils.vector import Vector
from game.common.player import Player
from game.common.team_manager import TeamManager
from game.common.enums import ActionType, CountryType


class TestSwapController(unittest.TestCase):
    """
    `Test Swap Controller:`

        This class tests the Swap Controller for swapping up and down with other characters, no
    """

    def setUp(self) -> None:
        self.swap_controller: SwapController = SwapController()
        self.team_manager: TeamManager = TeamManager([Character(name='Reginald', position=Vector(0, 0)),
                                                      Character(name='Count Leopold Von Liechtenstein III',
                                                                position=Vector(0, 1)),
                                                      Character(name='Bob', position=Vector(0, 2))])
        self.client = Player(None, None, [], self.team_manager)
        self.locations = {Vector(0, 0): [self.client.team_manager.team[0]],
                          Vector(0, 1): [self.client.team_manager.team[1]],
                          Vector(0, 2): [self.client.team_manager.team[2]]}
        self.game_board = GameBoard(0, Vector(2, 3), self.locations, False, self.client.team_manager)
        self.game_board.generate_map()

    # test swap up
    def test_swap_up_character(self) -> None:
        self.client.team_manager.team[0].took_action = True
        self.client.team_manager.team[1].took_action = True
        self.client.team_manager.team[2].took_action = False
        self.swap_controller.handle_actions(ActionType.SWAP_UP, self.client, self.game_board)

        self.assertEqual(self.client.team_manager.team[2].position, Vector(0, 1))
        self.assertEqual(self.client.team_manager.team[1].position, Vector(0, 2))
        self.assertEqual(self.game_board.get_characters(CountryType.URODA)[Vector(0, 1)].name, 'Bob')
        self.assertEqual(self.game_board.get_characters(CountryType.URODA)[Vector(0, 2)].name,
                         'Count Leopold Von Liechtenstein III')

    def test_swap_up_none(self) -> None:
        self.game_board.remove_coordinate(self.client.team_manager.team.pop(1).position)
        self.client.team_manager.team[0].took_action = True
        self.client.team_manager.team[1].took_action = False
        self.swap_controller.handle_actions(ActionType.SWAP_UP, self.client, self.game_board)
        self.assertEqual(self.client.team_manager.team[1].position, Vector(0, 1))
        self.assertEqual(self.game_board.get_characters(CountryType.URODA)[Vector(0, 1)].name, 'Bob')
        with self.assertRaises(KeyError):
            self.game_board.get_characters(CountryType.URODA)[Vector(0, 2)].name

    def test_swap_up_fail(self) -> None:
        self.client.team_manager.team[0].took_action = False
        self.client.team_manager.team[1].took_action = True
        self.client.team_manager.team[2].took_action = True
        self.swap_controller.handle_actions(ActionType.SWAP_UP, self.client, self.game_board)

        self.assertEqual(self.client.team_manager.team[0].position, Vector(0, 0))
        self.assertEqual(self.game_board.get_characters(CountryType.URODA)[Vector(0, 0)].name, 'Reginald')

    # test swap down
    def test_swap_down_character(self) -> None:
        self.client.team_manager.team[0].took_action = True
        self.client.team_manager.team[1].took_action = False
        self.client.team_manager.team[2].took_action = True
        self.swap_controller.handle_actions(ActionType.SWAP_DOWN, self.client, self.game_board)

        self.assertEqual(self.client.team_manager.team[1].position, Vector(0, 2))
        self.assertEqual(self.client.team_manager.team[2].position, Vector(0, 1))
        self.assertEqual(self.game_board.get_characters(CountryType.URODA)[Vector(0, 1)].name, 'Bob')
        self.assertEqual(self.game_board.get_characters(CountryType.URODA)[Vector(0, 2)].name,
                         'Count Leopold Von Liechtenstein III')

    def test_swap_down_none(self) -> None:
        self.game_board.remove_coordinate(self.client.team_manager.team.pop(1).position)
        self.client.team_manager.team[0].took_action = False
        self.client.team_manager.team[1].took_action = True
        self.swap_controller.handle_actions(ActionType.SWAP_DOWN, self.client, self.game_board)
        self.assertEqual(self.client.team_manager.team[0].position, Vector(0, 1))
        self.assertEqual(self.game_board.get_characters(CountryType.URODA)[Vector(0, 1)].name, 'Reginald')
        with self.assertRaises(KeyError):
            self.game_board.get_characters(CountryType.URODA)[Vector(0, 0)].name

    def test_swap_down_fail(self) -> None:
        self.client.team_manager.team[0].took_action = True
        self.client.team_manager.team[1].took_action = True
        self.client.team_manager.team[2].took_action = False
        self.swap_controller.handle_actions(ActionType.SWAP_DOWN, self.client, self.game_board)

        self.assertEqual(self.client.team_manager.team[2].position, Vector(0, 2))
        self.assertEqual(self.game_board.get_characters(CountryType.URODA)[Vector(0, 2)].name, 'Bob')