import unittest

from game.common.team_manager import TeamManager
from game.byte_2025.character import *
from game.common.enums import *
from game.common.action import *


class TestTeamManager(unittest.TestCase):
    """
    Test for Team Manager class
    """
    def setUp(self):
        self.character1: Character = Leader('Agles', CharacterType.TANK, 100, 10, 10, 10)
        self.character2: Character = GenericAttacker('Grog',health=50, attack=15, defense=5, speed=5)
        self.character3: Character = GenericHealer('Eden', health=60, attack=5, defense=15, speed=5)
        self.team_manager: TeamManager = TeamManager()
        self.team_manager2: TeamManager = TeamManager([self.character1, self.character2, self.character3])

    def test_init_default(self) -> None:
        self.assertEqual(self.team_manager.object_type, ObjectType.TEAMMANAGER)
        self.assertEqual(self.team_manager.team, TeamManager().team)
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
                                           f'and has the value of {2}.')
        with self.assertRaises(ValueError) as e:
            self.team_manager.team = 1
        self.assertEqual(str(e.exception), f'{self.team_manager.__class__.__name__}.team must be a list[Character]. '
                                           f'It is a(n) {int.__name__} '
                                           f'and has the value of {1}.')
        with self.assertRaises(ValueError) as e:
            self.team_manager.team = [self.character1, self.character2, 3]
        self.assertEqual(str(e.exception), f'{self.team_manager.__class__.__name__}.team must be a list[Character]. '
                                           f'It contains a(n) {int.__name__} with the value {3}.')
        with self.assertRaises(ValueError) as e:
            self.team_manager.team = [self.character1, self.character2, self.character3, self.character1]
        self.assertEqual(str(e.exception), f'{self.team_manager.__class__.__name__}.team must be a list[Character] '
                                           f'with a length of three or less. It has a length of {4}.')
        with self.assertRaises(ValueError) as e:
            self.team_manager.score = 'hi'
        self.assertEqual(str(e.exception), f'{self.team_manager.__class__.__name__}.score must be an int. '
                                           f'It is a(n) {str.__name__} and has the value of hi.')
        