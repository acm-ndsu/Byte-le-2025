import unittest

from game.byte_2025.character.character import *
from game.common.enums import ObjectType, CountryType
from game.common.map.wall import Wall
from game.common.team_manager import TeamManager
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
        self.leader: Leader = Leader(position=Vector(1, 2), country_type=CountryType.TURPIS)
        self.attacker: GenericAttacker = GenericAttacker(position=Vector(1, 3))

        # self.avatar: TeamManager = TeamManager()
        self.locations: dict[Vector, list[GameObject]] = {
            Vector(1, 1): [self.wall],
            Vector(1, 2): [self.leader],
            Vector(1, 3): [self.attacker],
        }

        self.ga1: GenericAttacker = GenericAttacker(speed=6)
        self.gh1: GenericHealer = GenericHealer(speed=3)
        self.gt1: GenericTank = GenericTank(speed=2)

        self.ga2: GenericAttacker = GenericAttacker(speed=5)
        self.gh2: GenericHealer = GenericHealer(speed=4)
        self.gt2: GenericTank = GenericTank(speed=1)

        self.uroda_team: list[Character] = [self.ga1, self.gh1, self.gt1]
        self.turpis_team: list[Character] = [self.ga2, self.gh2, self.gt2]

        uroda_manager: TeamManager = TeamManager(country=CountryType.URODA, team=self.uroda_team)
        turpis_manager: TeamManager = TeamManager(country=CountryType.TURPIS, team=self.turpis_team)

        self.game_board: GameBoard = GameBoard(1, Vector(3, 3), self.locations, False,
                                               uroda_team_manager=uroda_manager,
                                               turpis_team_manager=turpis_manager)

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

    def test_get_characters(self):
        characters: dict[Vector, Character] = self.game_board.get_characters()
        self.assertEqual(characters[Vector(1, 2)], self.leader)
        self.assertEqual(characters[Vector(1, 3)], self.attacker)
        self.assertEqual(len(characters), 2)

    def test_get_characters_by_country(self):
        characters: dict[Vector, Character] = self.game_board.get_characters(CountryType.TURPIS)
        self.assertEqual(characters[Vector(1, 2)], self.leader)
        self.assertEqual(len(characters), 1)

    # uroda has 3 characters, turpis has 3
    def test_order_characters_3x3(self):
        self.game_board.order_teams()
        self.assertEqual(self.game_board.ordered_teams, [(self.ga1, self.ga2), (self.gh1, self.gh2),
                                                         (self.gt1, self.gt2)])

    # uroda has 3 characters, turpis has 2
    def test_order_characters_3x2(self):
        self.turpis_team = self.turpis_team[:2]
        self.game_board.turpis_team_manager.team = self.turpis_team

        self.game_board.order_teams()
        self.assertEqual(self.game_board.ordered_teams, [(self.ga1, self.ga2), (self.gh1, self.gh2),
                                                         (self.gt1, None)])

    # uroda has 3 characters, turpis has 1
    def test_order_character_3x1(self):
        self.turpis_team = self.turpis_team[:1]
        self.game_board.turpis_team_manager.team = self.turpis_team

        self.game_board.order_teams()
        self.assertEqual(self.game_board.ordered_teams, [(self.ga1, self.ga2), (self.gh1, None),
                                                         (self.gt1, None)])

    # uroda has 2 characters, turpis has 3
    def test_order_character_2x3(self):
        self.uroda_team = self.uroda_team[:2]
        self.game_board.uroda_team_manager.team = self.uroda_team

        self.game_board.order_teams()
        self.assertEqual(self.game_board.ordered_teams, [(self.ga1, self.ga2), (self.gh1, self.gh2),
                                                         (None, self.gt2)])

    # uroda has 2 characters, turpis has 3
    def test_order_character_1x3(self):
        self.uroda_team = self.uroda_team[:1]
        self.game_board.uroda_team_manager.team = self.uroda_team

        self.game_board.order_teams()
        self.assertEqual(self.game_board.ordered_teams, [(self.ga1, self.ga2), (None, self.gh2),
                                                         (None, self.gt2)])

    # uroda has 2 characters, turpis has 2
    def test_order_character_2x2(self):
        self.uroda_team = self.uroda_team[:2]
        self.game_board.uroda_team_manager.team = self.uroda_team

        self.turpis_team = self.turpis_team[:2]
        self.game_board.turpis_team_manager.team = self.turpis_team

        self.game_board.order_teams()
        self.assertEqual(self.game_board.ordered_teams, [(self.ga1, self.ga2), (self.gh1, self.gh2)])

    # uroda has 2 characters, turpis has 1
    def test_order_character_2x1(self):
        self.uroda_team = self.uroda_team[:2]
        self.game_board.uroda_team_manager.team = self.uroda_team

        self.turpis_team = self.turpis_team[:1]
        self.game_board.turpis_team_manager.team = self.turpis_team

        self.game_board.order_teams()
        self.assertEqual(self.game_board.ordered_teams, [(self.ga1, self.ga2), (self.gh1, None)])

    # uroda has 1 characters, turpis has 2
    def test_order_character_1x2(self):
        self.uroda_team = self.uroda_team[:1]
        self.game_board.uroda_team_manager.team = self.uroda_team

        self.turpis_team = self.turpis_team[:2]
        self.game_board.turpis_team_manager.team = self.turpis_team

        self.game_board.order_teams()
        self.assertEqual(self.game_board.ordered_teams, [(self.ga1, self.ga2), (None, self.gh2)])

    # uroda has 1 characters, turpis has 1
    def test_order_character_1x1(self):
        self.uroda_team = self.uroda_team[:1]
        self.game_board.uroda_team_manager.team = self.uroda_team

        self.turpis_team = self.turpis_team[:1]
        self.game_board.turpis_team_manager.team = self.turpis_team

        self.game_board.order_teams()
        self.assertEqual(self.game_board.ordered_teams, [(self.ga1, self.ga2)])

    def test_get_ordered_teams_as_list(self):
        self.assertEqual(self.game_board.get_ordered_teams_as_list(),
                         [self.ga1, self.ga2, self.gh2, self.gh1, self.gt1, self.gt2])

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

        # check that both team managers stored information correctly
        self.assertEqual(self.game_board.uroda_team_manager.object_type, temp.uroda_team_manager.object_type)
        self.assertEqual(self.game_board.uroda_team_manager.team, temp.uroda_team_manager.team)
        self.assertEqual(self.game_board.uroda_team_manager.score, temp.uroda_team_manager.score)
        self.assertEqual(self.game_board.uroda_team_manager.country, temp.uroda_team_manager.country)

        self.assertEqual(self.game_board.turpis_team_manager.object_type, temp.turpis_team_manager.object_type)
        self.assertEqual(self.game_board.turpis_team_manager.team, temp.turpis_team_manager.team)
        self.assertEqual(self.game_board.turpis_team_manager.score, temp.turpis_team_manager.score)
        self.assertEqual(self.game_board.turpis_team_manager.country, temp.turpis_team_manager.country)
