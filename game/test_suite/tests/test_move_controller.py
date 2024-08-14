import unittest
from unittest.mock import Mock

from game.byte_2025.character.character import GenericAttacker, GenericTank, GenericHealer
from game.byte_2025.character.stats import DefenseStat, SpeedStat, AttackStat
from game.byte_2025.moves import move_logic
from game.byte_2025.moves.moves import *
from game.byte_2025.moves.moveset import Moveset
from game.common.map.game_board import GameBoard
from game.common.player import Player
from game.common.team_manager import TeamManager
from game.controllers.move_controller import MoveController
from game.utils.vector import Vector


class TestMoveController(unittest.TestCase):
    """
    This is the test file for both the MoveController and the move_logic.py file since they work in tandem.
    """
    def setUp(self):
        self.move_controller: MoveController = MoveController()

        # WILL IMPLEMENT EFFECTS IN A NEW BRANCH; this one has a lot of major changes already; don't want a bloated PR
        self.moveset1: Moveset = Moveset((Attack('Baja Blast', TargetType.SINGLE_OPP, 0, None, 15),
                                          Buff('Baja Slurp', TargetType.SELF, 2, HealEffect(heal_points=10), 1),
                                          Debuff('Baja Dump', TargetType.ALL_OPPS, 3, None, -1, ObjectType.SPEED_STAT),
                                          Heal('Baja Blessing', TargetType.ALL_ALLIES, 4, None, 10)))

        self.moveset2: Moveset = Moveset((Heal('Water Halo', TargetType.ALLY_UP, 0, None, 15),
                                          Attack('Inferno', TargetType.ALL_OPPS, 0, None, 15),
                                          Heal('Healing Potion', TargetType.ALLY_DOWN, 0, None, 15),
                                          Debuff('Thunder Arrow', TargetType.SINGLE_OPP, 0, None, stage_amount=-1,
                                                 stat_to_affect=ObjectType.DEFENSE_STAT)))

        # create uroda team
        self.uroda_attacker: GenericAttacker = GenericAttacker(health=20, attack=AttackStat(), defense=DefenseStat(5),
                                                               speed=SpeedStat(15), position=Vector(0, 0),
                                                               country_type=CountryType.URODA, moveset=self.moveset1)
        self.uroda_attacker.special_points = 10

        self.uroda_healer: GenericHealer = GenericHealer(health=20, attack=AttackStat(), defense=DefenseStat(5),
                                                         speed=SpeedStat(10), position=Vector(0, 1),
                                                         country_type=CountryType.URODA, moveset=self.moveset2)
        self.uroda_tank: GenericTank = GenericTank(health=20, attack=AttackStat(), defense=DefenseStat(10),
                                                   speed=SpeedStat(5), position=Vector(0, 2),
                                                   country_type=CountryType.URODA)

        # create turpis team
        self.turpis_tank: GenericTank = GenericTank(health=20, attack=AttackStat(), defense=DefenseStat(10),
                                                    speed=SpeedStat(5), position=Vector(1, 0),
                                                    country_type=CountryType.TURPIS)
        self.turpis_attacker: GenericAttacker = GenericAttacker(health=20, attack=AttackStat(), defense=DefenseStat(5),
                                                                speed=SpeedStat(15), position=Vector(1, 1),
                                                                country_type=CountryType.TURPIS)
        self.turpis_healer: GenericHealer = GenericHealer(health=20, attack=AttackStat(), defense=DefenseStat(5),
                                                          speed=SpeedStat(10), position=Vector(1, 2),
                                                          country_type=CountryType.TURPIS)

        # Uroda on the left, Turpis on the right;
        # Left side from top to bottom: Urodan healer, attacker, tank
        # Right side from top to bottom: Turpisian attack, tank, healer
        self.locations: dict[Vector, list[GameObject]] = {Vector(0, 0): [self.uroda_attacker],
                                                          Vector(0, 1): [self.uroda_healer],
                                                          Vector(0, 2): [self.uroda_tank],
                                                          Vector(1, 0): [self.turpis_tank],
                                                          Vector(1, 1): [self.turpis_attacker],
                                                          Vector(1, 2): [self.turpis_healer]}

        # create a Player object with a TeamManager
        self.uroda_team_manager: TeamManager = TeamManager([self.uroda_attacker, self.uroda_healer, self.uroda_tank],
                                                           CountryType.URODA)
        self.client: Player = Player(team_manager=self.uroda_team_manager)

        self.gameboard: GameBoard = GameBoard(locations=self.locations, map_size=Vector(2, 3))
        self.gameboard.generate_map()

    def test_given_invalid_enum(self) -> None:
        # mock the handle_move_logic method to later check if it was ever called
        mock: Mock = Mock()
        move_logic.handle_move_logic = mock

        self.move_controller.handle_actions(ActionType.SWAP_UP, self.client, self.gameboard)

        # check that the Generic Tank wasn't affected at all
        self.assertEqual(self.turpis_tank.current_health, self.turpis_tank.max_health)

        # test passes if the handle_move_logic method was never called
        mock.assert_not_called()

    def test_opponent_takes_damage(self) -> None:
        self.move_controller.handle_actions(ActionType.USE_NA, self.client, self.gameboard)

        # check the Generic Tank took damage
        # ceiling(15 damage * x1 modifier) - 10 defense = 5 damage dealt
        self.assertEqual(self.turpis_tank.current_health, self.turpis_tank.max_health - 5)

        # attacker should have 11 special points
        self.assertEqual(self.uroda_attacker.special_points, 11)

    def test_opponent_health_stays_at_0(self) -> None:
        self.turpis_tank.current_health = 1
        self.move_controller.handle_actions(ActionType.USE_NA, self.client, self.gameboard)

        # the generic tank's health should be 0
        self.assertEqual(self.turpis_tank.current_health, 0)

    def test_user_heals_entire_team(self) -> None:
        # change health to 1 to test healing
        self.uroda_attacker.current_health = 1
        self.uroda_healer.current_health = 1

        self.move_controller.handle_actions(ActionType.USE_S3, self.client, self.gameboard)

        # 1 HP + healing of 10 = 11
        self.assertEqual(self.uroda_attacker.current_health, 11)
        self.assertEqual(self.uroda_healer.current_health, 11)
        self.assertEqual(self.uroda_tank.current_health,  20)

        # ensure the special points decreased
        self.assertEqual(self.uroda_attacker.special_points, 6)

    def test_user_heals_over_max_health(self) -> None:
        # test if going healing over the max health doesn't go over
        self.uroda_attacker.current_health = self.uroda_attacker.max_health - 1

        self.move_controller.handle_actions(ActionType.USE_S3, self.client, self.gameboard)

        # 1 HP + healing of 10 = 11
        self.assertEqual(self.uroda_attacker.max_health, self.uroda_attacker.current_health)

        self.assertEqual(self.uroda_attacker.special_points, 6)

    def test_self_buffing(self) -> None:
        # test that a character buffing itself works while the target is themselves
        self.move_controller.handle_actions(ActionType.USE_S1, self.client, self.gameboard)

        # check the stat was buffed properly; default value from constructor is the attack stat
        self.assertEqual(self.uroda_attacker.attack.stage, 1)
        self.assertEqual(self.uroda_attacker.attack.calculate_modifier(self.uroda_attacker.attack.stage), 1.5)
        self.assertEqual(self.uroda_attacker.attack.value, 1.5)

        # ensure the special points decreased
        self.assertEqual(self.uroda_attacker.special_points, 8)

    def test_heal_ally_up(self) -> None:
        # set urodan attacker health to be at 1 HP and to have already taken their turn
        self.uroda_attacker.current_health = 1
        self.uroda_attacker.took_action = True

        self.move_controller.handle_actions(ActionType.USE_NA, self.client, self.gameboard)

        # 1 + 15 = 16 HP
        self.assertEqual(self.uroda_attacker.current_health, 16)

        # ensure the special points increased; this is the healer, so it's special points are at 0
        self.assertEqual(self.uroda_healer.special_points, 1)

    def test_heal_ally_down(self) -> None:
        # set urodan attack to have taken their turn
        self.uroda_attacker.took_action = True

        # set urodan tank health to be at 1 HP and to have already taken their turn
        self.uroda_tank.current_health = 1
        self.uroda_tank.took_action = True

        self.move_controller.handle_actions(ActionType.USE_S2, self.client, self.gameboard)

        # 1 + 15 = 16 HP
        self.assertEqual(self.uroda_tank.current_health, 16)

    def test_no_enemy_targets_available(self) -> None:
        # create a mock object to more easily test this functionality
        # will test if the handle_move_logic method was called; if not, then test succeeds
        mock: Mock = Mock()
        move_logic.handle_move_logic = mock

        # remove the turpis tank from the map
        self.gameboard.remove_coordinate(self.turpis_tank.position)

        # attempt to attack a target
        self.move_controller.handle_actions(ActionType.USE_NA, self.client, self.gameboard)

        # to ensure nothing happened, mock and check if the handle_move_logic method was called
        mock.assert_not_called()

        # the urodan attacker attempted to attack in this case, so the special points should stay 10
        self.assertEqual(self.uroda_attacker.special_points, 10)

    def test_no_ally_target_available(self):
        mock: Mock = Mock()
        move_logic.handle_move_logic = mock

        # remove all urodan characters except the healer who is in the middle
        self.gameboard.remove_coordinate(self.uroda_attacker.position)
        self.gameboard.remove_coordinate(self.uroda_tank.position)
        self.uroda_team_manager.team.remove(self.uroda_tank)
        self.uroda_team_manager.team.remove(self.uroda_attacker)

        # attempt to use moves that target an ally above and below, and ensure the `handle_actions` method wasn't called
        # checks if using the normal attack worked (heal ally up)
        self.move_controller.handle_actions(ActionType.USE_NA, self.client, self.gameboard)
        mock.assert_not_called()

        # checks if using s2 works (heal ally down)
        self.move_controller.handle_actions(ActionType.USE_S2, self.client, self.gameboard)
        mock.assert_not_called()

        # the healer is the character that tried to act
        self.assertEqual(self.uroda_healer.special_points, 0)

    # explicit move_logic tests below ---------------------------------------------------------------------

    def test_calculate_modifier_effect(self):
        # the turpis healer has speed 10; at -1 (which would be applied by the debuff), value would be 10 * 0.667 = 7
        result: int = move_logic.calculate_modifier_effect(self.turpis_healer, self.moveset1.get_s2())

        self.assertEqual(result, 7)

    def test_debuff_modifier_is_applied(self):
        # testing to ensure a debuff is applied properly from move_logic.py
        self.uroda_attacker.took_action = True

        # using the healer's debuff attack
        self.move_controller.handle_actions(ActionType.USE_S3, self.client, self.gameboard)

        # check that the turpis attacker's defense decreased
        self.assertEqual(self.turpis_attacker.defense.stage, -1)

        # ceiling(5 * 0.667) = 4
        self.assertEqual(self.turpis_attacker.defense.value, 4)
        self.assertEqual(self.turpis_attacker.defense.calculate_modifier(self.turpis_attacker.defense.stage), 0.667)

