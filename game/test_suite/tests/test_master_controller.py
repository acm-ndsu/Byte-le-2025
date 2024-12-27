import unittest

from game.commander_clash.character.character import Character
from game.commander_clash.generation.character_generation import *
from game.common.enums import ActionType, CountryType
from game.common.map.game_board import GameBoard
from game.common.player import Player
from game.common.team_manager import TeamManager
from game.config import DEFEATED_SCORE
from game.controllers.master_controller import MasterController
from game.utils.vector import Vector


class TestMasterController(unittest.TestCase):
    """
    `Test Master Controller Notes:`

        Add tests to this class to tests any new functionality added to the Master Controller.
    """

    def setUp(self) -> None:
        self.master_controller = MasterController()

        # speed order pairings: (Uroda Healer, Fultra), (Uroda Healer2, Turpis Tank), (Ninlil, Turpis Tank 2)
        self.team_manager1: TeamManager = TeamManager([generate_generic_healer('Uroda Healer'), generate_ninlil(),
                                                       generate_generic_healer('Uroda Healer 2')],
                                                      country_type=CountryType.URODA)
        self.team_manager2: TeamManager = TeamManager([generate_generic_tank('Turpis Tank'), generate_fultra(),
                                                       generate_generic_tank('Turpis Tank 2')],
                                                      country_type=CountryType.TURPIS)

        # set the country type to turpis for team manager 2
        for char in self.team_manager2.team:
            char.country_type = CountryType.TURPIS

        self.team_managers: list[TeamManager] = [self.team_manager1, self.team_manager2]
        self.actions: list[ActionType] = [ActionType.USE_NM]

        self.locations: dict = {
            Vector(0, 0): [self.team_manager1.team[0]],
            Vector(0, 1): [self.team_manager1.team[1]],
            Vector(0, 2): [self.team_manager1.team[2]],
            Vector(1, 0): [self.team_manager2.team[0]],
            Vector(1, 1): [self.team_manager2.team[1]],
            Vector(1, 2): [self.team_manager2.team[2]],
        }

        # organize the speeds to get access to the fastest characters
        self.team_manager1.speed_sort()
        self.team_manager2.speed_sort()

        self.gameboard: GameBoard = GameBoard(map_size=Vector(2, 3), locations=self.locations, walled=False,
                                              uroda_team_manager=self.team_manager1,
                                              turpis_team_manager=self.team_manager2)

        self.client1: Player = Player(team_name='Uroda Player', team_manager=self.team_manager1, actions=self.actions)
        self.client2: Player = Player(team_name='Turpis Player', team_manager=self.team_manager2, actions=self.actions)

        # generate the game map
        self.gameboard.generate_map()

        self.master_controller.current_world_data = {'game_board': self.gameboard.to_json()}

    def test_turn_logic(self) -> None:
        uroda_active_char_name: str = self.client1.team_manager.get_active_character().name
        turpis_active_char_name: str = self.client2.team_manager.get_active_character().name

        self.master_controller.turn_logic([self.client1, self.client2], 0)

        uroda_active_char: Character = self.client1.team_manager.get_character(uroda_active_char_name)
        turpis_active_char: Character = self.client2.team_manager.get_character(turpis_active_char_name)

        # assert that only the characters that took their turn have the 'took_action' bool set to True
        self.assertTrue(uroda_active_char.took_action)
        self.assertFalse(self.team_manager1.team[1].took_action)
        self.assertFalse(self.team_manager1.team[2].took_action)

        self.assertTrue(turpis_active_char.took_action)
        self.assertFalse(self.team_manager2.team[1].took_action)
        self.assertFalse(self.team_manager2.team[2].took_action)

    def test_resetting_took_action_bool(self) -> None:
        # let every character perform an action normally
        for char in self.team_manager1.team:
            self.master_controller.turn_logic([self.client1, self.client2], 0)

        # if all characters took their turn, every character's took action bool should be false
        self.assertFalse(self.client1.team_manager.team[0].took_action)
        self.assertFalse(self.client1.team_manager.team[1].took_action)
        self.assertFalse(self.client1.team_manager.team[2].took_action)

        self.assertFalse(self.client2.team_manager.team[0].took_action)
        self.assertFalse(self.client2.team_manager.team[1].took_action)
        self.assertFalse(self.client2.team_manager.team[2].took_action)

    def test_dead_handling(self) -> None:
        # arrangements for the test
        t_tank_position: Vector = self.client2.team_manager.get_character('Turpis Tank').position

        # defeat the Turpis Tank and ensure it's handled appropriately
        self.gameboard.get_character_from(t_tank_position).current_health = 1

        # generate the game map
        self.gameboard.generate_map()
        self.master_controller.current_world_data = {'game_board': self.gameboard.to_json()}

        self.master_controller.turn_logic([self.client1, self.client2], 0)

        # read the json of the gameboard to receive all recent changes
        self.gameboard = GameBoard().from_json(self.master_controller.current_world_data['game_board'])

        # set the team managers to be the updated versions
        self.client1.team_manager = self.gameboard.uroda_team_manager
        self.client2.team_manager = self.gameboard.turpis_team_manager

        self.assertTrue(self.client2.team_manager.dead_team[0].name == 'Turpis Tank')
        self.assertTrue(len(self.client2.team_manager.team) == 2)
        self.assertTrue(len(self.client2.team_manager.dead_team) == 1)

        # the uroda client should still have points gained for defeated an opposing character
        self.assertEqual(self.client1.team_manager.score, DEFEATED_SCORE)

        self.assertTrue(len(self.gameboard.game_map) == 5)
