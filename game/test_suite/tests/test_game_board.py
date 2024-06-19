import unittest

from game.common.enums import ObjectType
from game.common.team_manager import TeamManager
from game.common.map.game_object_container import GameObjectContainer
from game.common.map.wall import Wall
from game.controllers.movement_controller import MovementController
from game.utils.vector import Vector
from game.common.game_object import GameObject
from game.common.map.game_board import GameBoard
from game.test_suite.utils import spell_check


class TestGameBoard(unittest.TestCase):
    """
    `Test Gameboard Notes:`

        This class tests the different methods in the Gameboard class. This file is worthwhile to look at to understand
        the GamebBoard class better if there is still confusion on it.

        *This class tests the Gameboard specifically when the map is generated.*
    """

    def setUp(self) -> None:
        # TEST TEAM MANAGER, GAME BOARD, PLAYER, CHARACTER, ALL WHEN IMPLEMENTED

        self.wall: Wall = Wall()
        # self.avatar: TeamManager = TeamManager()
        self.locations: dict[Vector, list[GameObject]] = {
            Vector(1, 1): [self.wall, ],
        }

        self.game_board: GameBoard = GameBoard(1, Vector(3, 3), self.locations, False)
        self.game_board.generate_map()

    # test that seed cannot be set after generate_map
    def test_seed_fail(self):
        with self.assertRaises(RuntimeError) as e:
            self.game_board.seed = 20
        self.assertTrue(spell_check(str(e.exception), 'GameBoard variables cannot be changed once '
                                                      'generate_map is run.', False))

    # test that map_size cannot be set after generate_map
    def test_map_size_fail(self):
        with self.assertRaises(RuntimeError) as e:
            self.game_board.map_size = Vector(1, 1)
        self.assertTrue(spell_check(str(e.exception), 'GameBoard variables cannot be changed once '
                                                      'generate_map is run.', False))

    # test that locations cannot be set after generate_map
    def test_locations_fail(self):
        with self.assertRaises(RuntimeError) as e:
            self.game_board.locations = self.locations
        self.assertTrue(spell_check(str(e.exception), 'GameBoard variables cannot be changed once '
                                                      'generate_map is run.', False))

    # test that locations raises RuntimeError even with incorrect data type
    def test_locations_incorrect_fail(self):
        with self.assertRaises(RuntimeError) as e:
            self.game_board.locations = Vector(1, 1)
        self.assertTrue(spell_check(str(e.exception), 'GameBoard variables cannot be changed once '
                                                      'generate_map is run.', False))

    # test that walled cannot be set after generate_map
    def test_walled_fail(self):
        with self.assertRaises(RuntimeError) as e:
            self.game_board.walled = False
        self.assertTrue(spell_check(str(e.exception), 'GameBoard variables cannot be changed once '
                                                      'generate_map is run.', False))

    # test that get_objects works correctly with walls
    def test_get_objects_wall(self):
        walls: list[tuple[Vector, list[GameObject]]] = self.game_board.get_objects(ObjectType.WALL)
        self.assertTrue(all(map(lambda wall: isinstance(wall[1][0], Wall), walls)))
        self.assertEqual(len(walls), 1)

    # test json method
    def test_game_board_json(self):
        data: dict = self.game_board.to_json()
        temp: GameBoard = GameBoard().from_json(data)

        self.assertEqual(self.game_board.seed, temp.seed)
        self.assertEqual(self.game_board.map_size, temp.map_size)
        self.assertEqual(self.game_board.walled, temp.walled)
        self.assertEqual(self.game_board.event_active, temp.event_active)

        self.assertEqual(self.game_board.game_map.keys(), temp.game_map.keys())
        self.assertTrue(self.game_board.game_map.values(), temp.game_map.values())
