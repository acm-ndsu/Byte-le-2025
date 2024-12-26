import unittest
from unittest.mock import Mock

from game.commander_clash.generation.character_generation import *
from game.commander_clash.moves import move_logic
from game.commander_clash.moves.moves import *
from game.common.enums import CountryType, ActionType
from game.common.map.game_board import GameBoard
from game.common.player import Player
from game.common.team_manager import TeamManager
from game.controllers.new_move_controller import NewMoveController
from game.controllers.swap_controller import SwapController
from game.utils.vector import Vector


class TestMoveController(unittest.TestCase):
    """
    This is the test file for both the MoveController and the move_logic.py file since they work in tandem.
    """

    def setUp(self):
        self.new_move_controller: NewMoveController = NewMoveController()
        self.swap_controller: SwapController = SwapController()

        self.attack_effect: AttackEffect = AttackEffect(TargetType.SELF, 10)
        self.heal_effect: HealEffect = HealEffect(TargetType.ADJACENT_ALLIES, 10)
        self.buff_effect: BuffEffect = BuffEffect(TargetType.ALL_OPPS, 1, ObjectType.SPEED_STAT)
        self.debuff_effect: DebuffEffect = DebuffEffect(TargetType.ENTIRE_TEAM, -1, ObjectType.SPEED_STAT)

        self.uroda_attacker: GenericAttacker = generate_generic_attacker('Uroda Attacker')
        self.uroda_attacker.selected_move = self.uroda_attacker.get_nm()
        self.uroda_attacker.country_type = CountryType.URODA

        self.uroda_healer: GenericHealer = generate_generic_healer('Uroda Healer')
        self.uroda_healer.selected_move = self.uroda_healer.get_nm()
        self.uroda_healer.country_type = CountryType.URODA

        self.uroda_tank: GenericTank = generate_generic_tank('Uroda Tank')
        self.uroda_tank.selected_move = self.uroda_tank.get_nm()
        self.uroda_tank.country_type = CountryType.URODA

        self.turpis_attacker: GenericAttacker = generate_generic_attacker('Turpis Attacker')
        self.turpis_attacker.selected_move = self.turpis_attacker.get_nm()
        self.turpis_attacker.country_type = CountryType.TURPIS

        self.turpis_tank: GenericTank = generate_generic_tank('Turpis Tank')
        self.turpis_tank.selected_move = self.turpis_tank.get_nm()
        self.turpis_tank.country_type = CountryType.TURPIS

        self.turpis_tank2: GenericTank = generate_generic_tank('Turpis Tank 2')
        self.turpis_tank2.selected_move = self.turpis_tank2.get_nm()
        self.turpis_tank2.country_type = CountryType.TURPIS

        # Uroda on the left, Turpis on the right;
        # Left side from top to bottom: Urodan attack, healer, tank
        # Right side from top to bottom: Turpisian attack, tank, tank2
        self.locations: dict[Vector, list[GameObject]] = {Vector(0, 0): [self.uroda_attacker],
                                                          Vector(0, 1): [self.uroda_healer],
                                                          Vector(0, 2): [self.uroda_tank],
                                                          Vector(1, 0): [self.turpis_attacker],
                                                          Vector(1, 1): [self.turpis_tank],
                                                          Vector(1, 2): [self.turpis_tank2]}

        # create a Player object with a TeamManager
        self.uroda_team_manager: TeamManager = TeamManager([self.uroda_attacker, self.uroda_healer, self.uroda_tank],
                                                           CountryType.URODA)
        self.turpis_team_manager: TeamManager = TeamManager(
            [self.turpis_attacker, self.turpis_tank, self.turpis_tank2],
            CountryType.TURPIS)

        self.uroda_client: Player = Player(team_manager=self.uroda_team_manager)
        self.turpis_client: Player = Player(team_manager=self.turpis_team_manager)
        self.clients: list[Player] = [self.uroda_client, self.turpis_client]

        self.gameboard: GameBoard = GameBoard(locations=self.locations, map_size=Vector(2, 3),
                                              uroda_team_manager=self.uroda_team_manager,
                                              turpis_team_manager=self.turpis_team_manager)

        self.gameboard.generate_map()

    def test_given_invalid_enum(self) -> None:
        # mock the handle_move_logic method to later check if it was ever called
        mock: Mock = Mock()
        move_logic.handle_move_logic = mock

        self.new_move_controller.handle_logic(self.clients, self.gameboard)

        # check that the Generic Tank wasn't affected at all
        self.assertEqual(self.turpis_tank.current_health, self.turpis_tank.max_health)

        # test passes if the handle_move_logic method was never called
        mock.assert_not_called()

    def test_speed_tie(self) -> None:
        # uroda attacker and turpis attacker should be attacking each other at the same time
        self.new_move_controller.handle_logic(self.clients, self.gameboard)

        # expected damage: ceil((45 + 5) * (1 - 30 / 100)) = 35
        self.assertTrue(self.uroda_attacker.current_health == self.turpis_attacker.current_health)
        self.assertTrue(self.uroda_attacker.current_health == self.uroda_attacker.max_health - 35)

        # both attackers should have +1 special points
        self.assertEqual(self.uroda_attacker.special_points, 1)
        self.assertEqual(self.turpis_attacker.special_points, 1)

        self.assertTrue(self.uroda_attacker.took_action)
        self.assertTrue(self.turpis_attacker.took_action)

    def test_speed_tie_both_defeated(self) -> None:
        # set the health of both attackers to be 1
        self.uroda_attacker.current_health = 1
        self.turpis_attacker.current_health = 1

        self.new_move_controller.handle_logic(self.clients, self.gameboard)

        # both should be dead and have 0 health
        self.assertTrue(self.uroda_attacker.current_health == self.turpis_attacker.current_health == 0)
        self.assertTrue(self.uroda_attacker.is_dead and self.turpis_attacker.is_dead)
        self.assertTrue(self.uroda_attacker.took_action)
        self.assertTrue(self.turpis_attacker.took_action)

    def test_defeated_before_taking_turn(self) -> None:
        # remove the uroda and turpis attacker from the ordered teams list
        self.gameboard.ordered_teams.pop(0)

        # set turpis tank health to 1
        self.turpis_tank.current_health = 1

        # uroda healer and turpis tank fight; healer is faster and should kill tank before it attacks
        self.new_move_controller.handle_logic(self.clients, self.gameboard)

        # ensure the tank is dead and that the healer took no damage
        self.assertTrue(self.turpis_tank.current_health == 0 and self.turpis_tank.is_dead)
        self.assertFalse(self.turpis_tank.took_action)

        self.assertEqual(self.uroda_healer.current_health, self.uroda_healer.max_health)
        self.assertEqual(self.uroda_healer.special_points, 1)
        self.assertTrue(self.uroda_healer.took_action)

"""
Tests to do:
1. an aoe killing entire other team before any of them attack
2. attacking with a NM but no targets not increasing the special points
3. attacking with a special with no targets doesn't decrease the special points
4. everything else form the original test file 
"""
