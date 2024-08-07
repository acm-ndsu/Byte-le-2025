import unittest

from game.byte_2025.character import GenericAttacker, GenericTank
from game.byte_2025.moves.moves import *
from game.byte_2025.moves.moveset import Moveset
from game.common.map.game_board import GameBoard
from game.common.player import Player
from game.common.team_manager import TeamManager
from game.controllers.move_controller import MoveController
from game.utils.vector import Vector


class TestMoveController(unittest.TestCase):
    def setUp(self):
        self.move_controller: MoveController = MoveController()

        self.moveset: Moveset = Moveset((Attack('Baja Blast', TargetType.SINGLE_OPP, 0, None, 15),
                                        Buff('Baja Slurp', TargetType.SELF, 0, HealEffect(heal_points=10), 1.5),
                                        Debuff('Baja Dump', TargetType.ALL_OPPS, 0, None, 0.5),
                                        Heal('Baja Blessing', TargetType.ALL_ALLIES, 0, None, 10)))

        self.gen_attacker: GenericAttacker = GenericAttacker(health=20, defense=5, speed=15, position=Vector(0, 1),
                                                             country_type=CountryType.URODA, moveset=self.moveset)

        self.gen_tank: GenericTank = GenericTank(health=20, defense=10, speed=5, position=Vector(0, 1),
                                                 country_type=CountryType.TURPIS)

        # Uroda on the left, Turpis on the right; both characters are in the center of their respective sides
        self.locations: dict[Vector, list[GameObject]] = {Vector(0, 1): [self.gen_attacker],
                                                          Vector(1, 1): [self.gen_tank]}

        # create a Player object with a TeamManager
        self.uroda_team_manager: TeamManager = TeamManager([self.gen_attacker], CountryType.URODA)
        self.client: Player = Player(team_manager=self.uroda_team_manager)

        self.gameboard: GameBoard = GameBoard(locations=self.locations)
        self.gameboard.generate_map()

    def test_given_invalid_enum(self):
        self.move_controller.handle_actions(ActionType.SWAP_UP, self.client, self.gameboard)

        # check that the Generic Tank wasn't affected at all
        self.assertEqual(self.gen_tank.current_health, self.gen_tank.max_health)

        # check all stats after implementing stat system

    def test_opponent_takes_damage(self):
        self.move_controller.handle_actions(ActionType.USE_NA, self.client, self.gameboard)

        # check the Generic Tank took damage
        # 15 damage - 10 defense = 5 damage dealt

        # THIS TEST WILL BE MODIFIED WITH THE STAT CLASS IMPLEMENTATION
        self.assertEqual(self.gen_tank.current_health, self.gen_tank.max_health - 5)

    def test_opponent_health_stays_at_0(self):
        self.gen_tank.current_health = 1
        self.move_controller.handle_actions(ActionType.USE_NA, self.client, self.gameboard)

        # the generic tank's health should be 0

        self.assertEqual(self.gen_tank.current_health, 0)

    def test_user_heals_self(self):
        # to test healing
        self.gen_attacker.current_health = 1

        self.move_controller.handle_actions(ActionType.USE_S3, self.client, self.gameboard)

        # 1 HP + healing of 10 = 11
        self.assertEqual(self.gen_attacker.current_health, 11)

    def test_user_heals_over_max_health(self):
        # test if going healing over the max health doesn't go over
        self.gen_attacker.current_health = self.gen_attacker.max_health - 1

        self.move_controller.handle_actions(ActionType.USE_S3, self.client, self.gameboard)

        # 1 HP + healing of 10 = 11
        self.assertEqual(self.gen_attacker.max_health, self.gen_attacker.current_health)
