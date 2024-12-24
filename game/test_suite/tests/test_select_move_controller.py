import unittest
from unittest.mock import Mock

from game.commander_clash.character.character import GenericAttacker, GenericTank, GenericHealer
from game.commander_clash.character.stats import DefenseStat, SpeedStat, AttackStat
from game.commander_clash.moves import move_logic
from game.commander_clash.moves.moves import *
from game.commander_clash.moves.moveset import Moveset
from game.common.map.game_board import GameBoard
from game.common.player import Player
from game.common.team_manager import TeamManager
from game.common.enums import CountryType, ActionType
from game.controllers.move_controller import MoveController
from game.controllers.select_move_controller import SelectMoveController
from game.controllers.swap_controller import SwapController
from game.utils.vector import Vector


class TestSelectMoveController(unittest.TestCase):
    """
    This is the test file for testing the SelectMoveController.
    """

    def setUp(self):
        self.select_move_controller = SelectMoveController()

        self.attack_effect: AttackEffect = AttackEffect(TargetType.SELF, 10)
        self.heal_effect: HealEffect = HealEffect(TargetType.ADJACENT_ALLIES, 10)
        self.buff_effect: BuffEffect = BuffEffect(TargetType.ALL_OPPS, 1, ObjectType.SPEED_STAT)
        self.debuff_effect: DebuffEffect = DebuffEffect(TargetType.ENTIRE_TEAM, -1, ObjectType.SPEED_STAT)

        self.attacker_moveset: Moveset = Moveset(
            (Attack('Baja Blast', TargetType.SINGLE_OPP, 0, HealEffect(TargetType.ENTIRE_TEAM, 10), 5),
             Buff('Baja Slurp', TargetType.SELF, 2, HealEffect(heal_points=10), 1),
             Debuff('Baja Dump', TargetType.ALL_OPPS, 3, None, -1,
                    ObjectType.SPEED_STAT)))

        self.healer_moveset: Moveset = Moveset(
            (Heal('Water Halo', TargetType.ADJACENT_ALLIES, 0, self.attack_effect, 15),
             Attack('Inferno', TargetType.ALL_OPPS, 0, self.debuff_effect, 15),
             Debuff('Potion of Weakness', TargetType.SINGLE_OPP, 0, self.buff_effect, -1,
                    stat_to_affect=ObjectType.DEFENSE_STAT)))

        self.tank_moveset: Moveset = Moveset((Buff('Baja Barrier', TargetType.SELF, 0, None, 10),
                                              Attack('Break Bone', TargetType.SINGLE_OPP, 0, None, 15),
                                              Heal('Healing Potion', TargetType.ADJACENT_ALLIES, 0, None, 15)))

        # create uroda team
        self.uroda_attacker: GenericAttacker = GenericAttacker(health=20, attack=AttackStat(15), defense=DefenseStat(5),
                                                               speed=SpeedStat(15), position=Vector(0, 0),
                                                               country_type=CountryType.URODA,
                                                               moveset=self.attacker_moveset)
        self.uroda_attacker.special_points = 4

        self.uroda_healer: GenericHealer = GenericHealer(health=20, attack=AttackStat(5), defense=DefenseStat(5),
                                                         speed=SpeedStat(10), position=Vector(0, 1),
                                                         country_type=CountryType.URODA, moveset=self.healer_moveset)
        self.uroda_tank: GenericTank = GenericTank(health=20, attack=AttackStat(10), defense=DefenseStat(10),
                                                   speed=SpeedStat(5), position=Vector(0, 2),
                                                   country_type=CountryType.URODA, moveset=self.tank_moveset)

        # create turpis team
        self.turpis_attacker: GenericAttacker = GenericAttacker(health=20, attack=AttackStat(15),
                                                                defense=DefenseStat(5),
                                                                speed=SpeedStat(15), position=Vector(1, 1),
                                                                country_type=CountryType.TURPIS,
                                                                moveset=self.attacker_moveset)
        self.turpis_tank: GenericTank = GenericTank(health=20, attack=AttackStat(10), defense=DefenseStat(10),
                                                    speed=SpeedStat(5), position=Vector(1, 0),
                                                    country_type=CountryType.TURPIS, moveset=self.tank_moveset)
        self.turpis_healer: GenericHealer = GenericHealer(health=20, attack=AttackStat(5), defense=DefenseStat(5),
                                                          speed=SpeedStat(10), position=Vector(1, 2),
                                                          country_type=CountryType.TURPIS, moveset=self.healer_moveset)

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
        self.turpis_team_manager: TeamManager = TeamManager(
            [self.turpis_attacker, self.turpis_healer, self.turpis_tank],
            CountryType.TURPIS)
        self.uroda_client: Player = Player(team_manager=self.uroda_team_manager)
        self.turpis_client: Player = Player(team_manager=self.turpis_team_manager)

        self.gameboard: GameBoard = GameBoard(locations=self.locations, map_size=Vector(2, 3))

        # set the game board references to the team_managers
        self.gameboard.uroda_team_manager = self.uroda_team_manager
        self.gameboard.turpis_team_manager = self.turpis_team_manager

        self.gameboard.generate_map()

    def test_given_valid_enum(self) -> None:
        # the active character is the attacker, and it's selected move should be the normal move
        self.select_move_controller.handle_actions(ActionType.USE_NM, self.uroda_client, self.gameboard)

        # test that the attacker's selected move is the normal move
        self.assertEqual(self.uroda_attacker.selected_move.name, self.attacker_moveset.get_nm().name)

        # test that the gameboard's reference of the attacker also has correct selected move
        self.assertEqual(self.gameboard.uroda_team_manager.get_character(self.uroda_attacker.name).selected_move.name,
                         self.attacker_moveset.get_nm().name)

        # test special 1
        self.select_move_controller.handle_actions(ActionType.USE_S1, self.uroda_client, self.gameboard)
        self.assertEqual(self.uroda_attacker.selected_move.name, self.attacker_moveset.get_s1().name)
        self.assertEqual(self.gameboard.uroda_team_manager.get_character(self.uroda_attacker.name).selected_move.name,
                         self.attacker_moveset.get_s1().name)

        # test special 2
        self.select_move_controller.handle_actions(ActionType.USE_S2, self.uroda_client, self.gameboard)
        self.assertEqual(self.uroda_attacker.selected_move.name, self.attacker_moveset.get_s2().name)
        self.assertEqual(self.gameboard.uroda_team_manager.get_character(self.uroda_attacker.name).selected_move.name,
                         self.attacker_moveset.get_s2().name)

    def test_invalid_enum(self) -> None:
        # test that the selected move is None after receiving an invalid enum
        self.select_move_controller.handle_actions(ActionType.SWAP_UP, self.uroda_client, self.gameboard)
        self.assertTrue(self.uroda_attacker.selected_move is None)
        self.assertTrue(self.gameboard.uroda_team_manager.get_character(self.uroda_attacker.name).selected_move is None)
