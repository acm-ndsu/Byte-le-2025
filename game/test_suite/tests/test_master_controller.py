import unittest

from game.commander_clash.character.character import Character
from game.commander_clash.generation.character_generation import *
from game.common.enums import ActionType, CountryType
from game.common.map.game_board import GameBoard
from game.common.player import Player
from game.common.team_manager import TeamManager
from game.controllers.master_controller import MasterController
from game.controllers.move_controller import MoveController
from game.controllers.swap_controller import SwapController
from game.utils.generate_game import generate
from game.utils.vector import Vector


class TestMasterController(unittest.TestCase):
    """
    `Test Master Controller Notes:`

        Add tests to this class to tests any new functionality added to the Master Controller.
    """

    def setUp(self) -> None:
        self.master_controller = MasterController()
        self.swap_controller: SwapController = SwapController()
        self.move_controller: MoveController = MoveController()

        self.team_manager1: TeamManager = TeamManager([generate_generic_healer(), generate_ninlil(),
                                                       generate_generic_healer()], country_type=CountryType.URODA)
        self.team_manager2: TeamManager = TeamManager([generate_generic_tank(), generate_fultra(),
                                                       generate_generic_tank()], country_type=CountryType.TURPIS)

        self.team_managers: list[TeamManager] = [self.team_manager1, self.team_manager2]
        self.actions: list[ActionType] = [ActionType.USE_NM]

        self.client1: Player = Player(team_name='Uroda Player', team_manager=self.team_manager1, actions=self.actions)
        self.client2: Player = Player(team_name='Turpis Player', team_manager=self.team_manager2, actions=self.actions)

        self.locations: dict = {
            Vector(0, 0): [self.team_manager1.team[0]],
            Vector(0, 1): [self.team_manager1.team[1]],
            Vector(0, 2): [self.team_manager1.team[2]],
            Vector(1, 0): [self.team_manager2.team[0]],
            Vector(1, 1): [self.team_manager2.team[1]],
            Vector(1, 2): [self.team_manager2.team[2]],
        }

        self.gameboard: GameBoard = GameBoard(map_size=Vector(2, 3), locations=self.locations, walled=False,
                                              uroda_team_manager=self.team_manager1,
                                              turpis_team_manager=self.team_manager2)

        # generate the game map
        self.gameboard.generate_map()

        self.master_controller.current_world_data = {'game_board': self.gameboard.to_json()}

        # organize the speeds to get access to the fastest characters
        self.team_manager1.speed_sort()
        self.team_manager2.speed_sort()

    def test_turn_logic(self) -> None:
        uroda_active_char: Character = self.team_manager1.get_active_character()
        turpis_active_char: Character = self.team_manager2.get_active_character()

        self.master_controller.turn_logic([self.client1, self.client2], 0)

        # assert that only the active characters have took_action set to true
        self.assertTrue(uroda_active_char.took_action)
        self.assertFalse(self.team_manager1.team[1].took_action)
        self.assertFalse(self.team_manager1.team[2].took_action)

        self.assertTrue(turpis_active_char.took_action)
        self.assertFalse(self.team_manager2.team[1].took_action)
        self.assertFalse(self.team_manager2.team[2].took_action)
