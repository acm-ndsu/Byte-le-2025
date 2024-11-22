import unittest

from game.commander_clash.generation.character_generation import (generate_anahita, generate_berry,
                                                                  generate_generic_attacker, generate_generic_tank)
from game.common.team_manager import TeamManager
from game.controllers.master_controller import MasterController
from game.controllers.move_controller import MoveController
from game.controllers.swap_controller import SwapController


class TestMasterController(unittest.TestCase):
    """
    `Test Master Controller Notes:`

        Add tests to this class to tests any new functionality added to the Master Controller.
    """

    def setUp(self) -> None:
        self.master_controller = MasterController()
        self.swap_controller: SwapController = SwapController()
        self.move_controller: MoveController = MoveController()

        self.team_manager1: TeamManager = TeamManager([generate_anahita(), generate_generic_attacker(),
                                                       generate_generic_attacker()])
        self.team_manager2: TeamManager = TeamManager([generate_berry(), generate_generic_tank(),
                                                       generate_generic_tank()])


