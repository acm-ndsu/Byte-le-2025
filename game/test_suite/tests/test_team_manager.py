import unittest

from game.byte_2025.character import *
from game.common.action import *
from game.common.team_manager import TeamManager


class TestTeamManager(unittest.TestCase):
    """
    Test for Team Manager class
    """
    def setUp(self):
        self.character1: Character = Leader('Agles', CharacterType.TANK, 100, 10, 10, 5)
        self.character2: Character = GenericAttacker('Grog', health=50, attack=15, defense=5, speed=15)
        self.character3: Character = GenericHealer('Eden', health=60, attack=5, defense=15, speed=10)
        self.team_manager: TeamManager = TeamManager()
        self.team_manager2: TeamManager = TeamManager()
        self.team_manager2.team = [self.character1, self.character2, self.character3]

    def test_init_default(self) -> None:
        self.assertEqual(self.team_manager.object_type, ObjectType.TEAMMANAGER)
        self.assertEqual(len(self.team_manager.team), 3)
        self.assertEqual(self.team_manager.score, 0)

    def test_init_unique(self) -> None:
        self.assertEqual(self.team_manager2.object_type, ObjectType.TEAMMANAGER)
        self.assertEqual(self.team_manager2.team, [self.character1, self.character2, self.character3])
        self.assertEqual(self.team_manager2.score, 0)

    def test_setters(self) -> None:
        with self.assertRaises(ValueError) as e:
            self.team_manager.object_type = 2
        self.assertEqual(str(e.exception), f'{self.team_manager.__class__.__name__}.object_type must be an '
                                           f'ObjectType. It is a(n) {int.__name__} '
                                           f'and has the value of 2.')
        with self.assertRaises(ValueError) as e:
            self.team_manager.team = 1
        self.assertEqual(str(e.exception), f'{self.team_manager.__class__.__name__}.team must be a list[Character]. '
                                           f'It is a(n) {int.__name__} '
                                           f'and has the value of 1.')
        with self.assertRaises(ValueError) as e:
            self.team_manager.team = [self.character1, self.character2, 3]
        self.assertEqual(str(e.exception), f'{self.team_manager.__class__.__name__}.team must be a list[Character]. '
                                           f'It contains a(n) {int.__name__} with the value 3.')
        with self.assertRaises(ValueError) as e:
            self.team_manager.team = [self.character1, self.character2, self.character3, self.character1]
        self.assertEqual(str(e.exception), f'{self.team_manager.__class__.__name__}.team must be a list[Character] '
                                           f'with a length of three or less. It has a length of 4.')
        with self.assertRaises(ValueError) as e:
            self.team_manager.score = 'hi'
        self.assertEqual(str(e.exception), f'{self.team_manager.__class__.__name__}.score must be an int. '
                                           f'It is a(n) {str.__name__} and has the value of hi.')

    def test_speed_sort(self) -> None:
        self.team_manager2.speed_sort()
        self.assertEqual(self.team_manager2.team, [self.character2, self.character3, self.character1])

    def test_filter_by_type(self) -> None:
        self.assertEqual(len(self.team_manager.filter_by_type(CharacterType.ATTACKER)), 3)
        self.assertEqual(self.team_manager.filter_by_type(CharacterType.TANK), [])
        self.assertEqual(self.team_manager2.filter_by_type(CharacterType.TANK), [self.character1])
        self.assertEqual(self.team_manager2.filter_by_type(CharacterType.ATTACKER), [self.character2])
        self.assertEqual(self.team_manager2.filter_by_type(CharacterType.HEALER), [self.character3])

    def test_json_default(self) -> None:
        data: dict = self.team_manager.to_json()
        team_manager: TeamManager = TeamManager().from_json(data)
        self.assertEqual(team_manager.object_type, self.team_manager.object_type)
        self.assertEqual(team_manager.team, self.team_manager.team)
        self.assertEqual(team_manager.score, self.team_manager.score)

    def test_json_unique(self) -> None:
        data: dict = self.team_manager2.to_json()
        team_manager2: TeamManager = TeamManager().from_json(data)
        self.assertEqual(team_manager2.object_type, self.team_manager2.object_type)
        self.assertEqual(team_manager2.team, self.team_manager2.team)
        self.assertEqual(team_manager2.score, self.team_manager2.score)