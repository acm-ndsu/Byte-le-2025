import unittest

from game.commander_clash.character.character import *
from game.common.action import *
from game.common.team_manager import TeamManager
from game.controllers.swap_controller import SwapController


class TestTeamManager(unittest.TestCase):
    """
    Test for Team Manager class
    """

    def setUp(self):
        self.leader: Leader = Leader('Agles', CharacterType.TANK, 100, AttackStat(), DefenseStat(10),
                                     SpeedStat(5))
        self.attacker: GenericAttacker = GenericAttacker('Grog', health=50, attack=AttackStat(), defense=DefenseStat(5),
                                                         speed=SpeedStat(15))
        self.healer: GenericHealer = GenericHealer('Eden', health=60, attack=AttackStat(), defense=DefenseStat(15),
                                                   speed=SpeedStat(10))
        self.team_manager: TeamManager = TeamManager()
        self.team_manager2: TeamManager = TeamManager([self.leader, self.attacker, self.healer],
                                                      CountryType.TURPIS)

        self.swap_controller: SwapController = SwapController()

    def test_init_default(self) -> None:
        self.assertEqual(self.team_manager.object_type, ObjectType.TEAMMANAGER)
        self.assertEqual(self.team_manager.team, TeamManager().team)
        self.assertEqual(self.team_manager.score, 0)

    def test_init_unique(self) -> None:
        self.assertEqual(self.team_manager2.object_type, ObjectType.TEAMMANAGER)
        self.assertEqual(self.team_manager2.team, [self.leader, self.attacker, self.healer])
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
            self.team_manager.team = [self.leader, self.attacker, 3]
        self.assertEqual(str(e.exception), f'{self.team_manager.__class__.__name__}.team must be a list[Character]. '
                                           f'It contains a(n) {int.__name__} with the value 3.')
        with self.assertRaises(ValueError) as e:
            self.team_manager.team = [self.leader, self.attacker, self.healer, self.leader]
        self.assertEqual(str(e.exception), f'{self.team_manager.__class__.__name__}.team must be a list[Character] '
                                           f'with a length of three or less. It has a length of 4.')
        with self.assertRaises(ValueError) as e:
            self.team_manager.score = 'hi'
        self.assertEqual(str(e.exception), f'{self.team_manager.__class__.__name__}.score must be an int. '
                                           f'It is a(n) {str.__name__} and has the value of hi.')

    def test_speed_sort(self) -> None:
        self.team_manager2.speed_sort()
        self.assertEqual(self.team_manager2.team, [self.attacker, self.healer, self.leader])

    def test_filter_by_type(self) -> None:
        self.assertEqual(self.team_manager.filter_by_type(CharacterType.ATTACKER), TeamManager().team)
        self.assertEqual(self.team_manager.filter_by_type(CharacterType.TANK), [])
        self.assertEqual(self.team_manager2.filter_by_type(CharacterType.TANK), [self.leader])
        self.assertEqual(self.team_manager2.filter_by_type(CharacterType.ATTACKER), [self.attacker])
        self.assertEqual(self.team_manager2.filter_by_type(CharacterType.HEALER), [self.healer])

    def test_get_active_character(self) -> None:
        # the team needs to be ordered by speed to get the correct result
        self.team_manager2.speed_sort()
        self.assertEqual(self.team_manager2.get_active_character(), self.attacker)
        self.attacker.took_action = True

        self.assertEqual(self.team_manager2.get_active_character(), self.healer)
        self.healer.took_action = True

        self.assertEqual(self.team_manager2.get_active_character(), self.leader)
        self.leader.took_action = True

    def test_json_default(self) -> None:
        data: dict = self.team_manager.to_json()
        team_manager: TeamManager = TeamManager().from_json(data)
        self.assertEqual(team_manager.object_type, self.team_manager.object_type)
        # self.assertEqual(team_manager.team, self.team_manager.team)
        self.assertEqual(team_manager.country, self.team_manager.country)
        self.assertEqual(team_manager.score, self.team_manager.score)

        [self.assertTrue(team_manager.team[x] == self.team_manager.team[x]) for
         x in range(len(self.team_manager.team))]

    def test_json_unique(self) -> None:
        data: dict = self.team_manager2.to_json()
        team_manager2: TeamManager = TeamManager().from_json(data)
        self.assertEqual(team_manager2.object_type, self.team_manager2.object_type)
        self.assertEqual(team_manager2.country, self.team_manager2.country)
        self.assertEqual(team_manager2.score, self.team_manager2.score)

        [self.assertTrue(team_manager2.team[x] == self.team_manager2.team[x]) for
         x in range(len(self.team_manager2.team))]
