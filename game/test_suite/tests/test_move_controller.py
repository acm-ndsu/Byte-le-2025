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
from game.controllers.move_controller import MoveController
from game.controllers.swap_controller import SwapController
from game.utils.vector import Vector


class TestMoveController(unittest.TestCase):
    """
    This is the test file for both the MoveController and the move_logic.py file since they work in tandem.
    """

    def setUp(self):
        self.move_controller: MoveController = MoveController()
        self.swap_controller: SwapController = SwapController()

        self.attack_effect: AttackEffect = AttackEffect(TargetType.SELF, 10)
        self.heal_effect: HealEffect = HealEffect(TargetType.ADJACENT_ALLIES, 10)
        self.buff_effect: BuffEffect = BuffEffect(TargetType.ALL_OPPS, 1, ObjectType.SPEED_STAT)
        self.debuff_effect: DebuffEffect = DebuffEffect(TargetType.ALL_ALLIES, -1, ObjectType.SPEED_STAT)

        self.attacker_moveset: Moveset = Moveset((Attack('Baja Blast', TargetType.SINGLE_OPP, 0, None, 5),
                                                  Buff('Baja Slurp', TargetType.SELF, 2, HealEffect(heal_points=10), 5),
                                                  Debuff('Baja Dump', TargetType.ALL_OPPS, 3, None, -1,
                                                         ObjectType.SPEED_STAT),
                                                  Heal('Baja Blessing', TargetType.ALL_ALLIES, 4, None, 10)))

        self.healer_moveset: Moveset = Moveset(
            (Heal('Water Halo', TargetType.ADJACENT_ALLIES, 0, self.attack_effect, 15),
             Attack('Inferno', TargetType.ALL_OPPS, 0, self.heal_effect, 15),
             Heal('Healing Potion', TargetType.ADJACENT_ALLIES, 0, self.buff_effect, 15),
             Debuff('Thunder Arrow', TargetType.SINGLE_OPP, 0, self.debuff_effect,
                    debuff_amount=-1, stat_to_affect=ObjectType.DEFENSE_STAT)))

        self.tank_moveset: Moveset = Moveset((Guard('Baja Barrier', 0),
                                              Attack('Break Bone', TargetType.SINGLE_OPP, 0, None, 15),
                                              Heal('Healing Potion', TargetType.ADJACENT_ALLIES, 0, None, 15),
                                              Debuff('Thunder Arrow', TargetType.SINGLE_OPP, 0, None, debuff_amount=-1,
                                                     stat_to_affect=ObjectType.DEFENSE_STAT)))

        # create uroda team
        self.uroda_attacker: GenericAttacker = GenericAttacker(health=20, attack=AttackStat(15), defense=DefenseStat(5),
                                                               speed=SpeedStat(15), position=Vector(0, 0),
                                                               country_type=CountryType.URODA,
                                                               moveset=self.attacker_moveset)
        self.uroda_attacker.special_points = 10

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
        self.gameboard.generate_map()

    def test_given_invalid_enum(self) -> None:
        # mock the handle_move_logic method to later check if it was ever called
        mock: Mock = Mock()
        move_logic.handle_move_logic = mock

        self.move_controller.handle_actions(ActionType.SWAP_UP, self.uroda_client, self.gameboard)

        # check that the Generic Tank wasn't affected at all
        self.assertEqual(self.turpis_tank.current_health, self.turpis_tank.max_health)

        # test passes if the handle_move_logic method was never called
        mock.assert_not_called()

    def test_opponent_takes_damage(self) -> None:
        self.move_controller.handle_actions(ActionType.USE_NM, self.uroda_client, self.gameboard)

        # The uroda attacker is attacking the turpis tank
        # check the Generic Tank took damage: ceil((15 + 5) * (1 - 10 / 100)) = 18
        self.assertEqual(self.turpis_tank.current_health, self.turpis_tank.max_health - 18)

        # uroda attacker should have 11 special points
        self.assertEqual(self.uroda_attacker.special_points, 11)

    def test_opponent_health_stays_at_0(self) -> None:
        self.turpis_tank.current_health = 1

        # The uroda attacker is attacking the turpis tank
        self.move_controller.handle_actions(ActionType.USE_NM, self.uroda_client, self.gameboard)

        # the generic tank's health should be 0
        self.assertEqual(self.turpis_tank.current_health, 0)

    def test_user_heals_entire_team(self) -> None:
        # change health to 1 to test healing
        self.uroda_attacker.current_health = 1
        self.uroda_healer.current_health = 1

        self.move_controller.handle_actions(ActionType.USE_S3, self.uroda_client, self.gameboard)

        # 1 HP + healing of 10 = 11
        self.assertEqual(self.uroda_attacker.current_health, 11)
        self.assertEqual(self.uroda_healer.current_health, 11)
        self.assertEqual(self.uroda_tank.current_health, 20)

        # ensure the special points decreased
        self.assertEqual(self.uroda_attacker.special_points, 6)

    def test_user_heals_over_max_health(self) -> None:
        # test if going healing over the max health doesn't go over
        self.uroda_attacker.current_health = self.uroda_attacker.max_health - 1

        self.move_controller.handle_actions(ActionType.USE_S3, self.uroda_client, self.gameboard)

        # 1 HP + healing of 10 = 11
        self.assertEqual(self.uroda_attacker.max_health, self.uroda_attacker.current_health)

        self.assertEqual(self.uroda_attacker.special_points, 6)

    def test_self_buffing(self) -> None:
        # test that a character buffing itself works while the target is themselves
        # uroda attack buffs themselves
        self.move_controller.handle_actions(ActionType.USE_S1, self.uroda_client, self.gameboard)

        # check the stat was buffed properly; default value from constructor is the attack stat
        self.assertEqual(self.uroda_attacker.attack.value, 20)

        # ensure the special points decreased
        self.assertEqual(self.uroda_attacker.special_points, 8)

    def test_heal_ally_up(self) -> None:
        # set urodan attacker health to be at 1 HP and to have already taken their turn
        self.uroda_attacker.current_health = 1
        self.uroda_attacker.took_action = True

        self.move_controller.handle_actions(ActionType.USE_NM, self.uroda_client, self.gameboard)

        # 1 + 15 = 16 HP
        self.assertEqual(self.uroda_attacker.current_health, 16)

        # ensure the special points increased; this is the healer, so it's special points are at 0
        self.assertEqual(self.uroda_healer.special_points, 1)

    def test_heal_adjacent_allies(self) -> None:
        # set urodan attack to have taken their turn and to be on 1 HP
        self.uroda_attacker.current_health = 1
        self.uroda_attacker.took_action = True

        # set urodan tank health to be at 1 HP and to have already taken their turn
        self.uroda_tank.current_health = 1
        self.uroda_tank.took_action = True

        self.move_controller.handle_actions(ActionType.USE_S2, self.uroda_client, self.gameboard)

        # Tank's health: 1 + 15 = 16 HP
        self.assertEqual(self.uroda_tank.current_health, 16)

        # attacker's health: 1 + 15 = 16 HP
        self.assertEqual(self.uroda_tank.current_health, 16)

    def test_no_enemy_targets_available(self) -> None:
        # create a mock object to more easily test this functionality
        # will test if the handle_move_logic method was called; if not, then test succeeds
        mock: Mock = Mock()
        move_logic.handle_move_logic = mock

        # remove the turpis tank from the map
        self.gameboard.remove_coordinate(self.turpis_tank.position)

        # attempt to attack a target
        self.move_controller.handle_actions(ActionType.USE_NM, self.uroda_client, self.gameboard)

        # to ensure nothing happened, mock and check if the handle_move_logic method was called
        mock.assert_not_called()

        # the urodan attacker attempted to attack in this case, so the special points should stay 10
        self.assertEqual(self.uroda_attacker.special_points, 10)

    def test_no_ally_target_available(self) -> None:
        mock: Mock = Mock()
        move_logic.handle_move_logic = mock

        # remove all urodan characters except the healer who is in the middle
        self.gameboard.remove_coordinate(self.uroda_attacker.position)
        self.gameboard.remove_coordinate(self.uroda_tank.position)
        self.uroda_team_manager.team.remove(self.uroda_tank)
        self.uroda_team_manager.team.remove(self.uroda_attacker)

        # attempt to use moves that target an ally above and below, and ensure the `handle_actions` method wasn't called
        # checks if using the normal attack worked (heal ally up)
        self.move_controller.handle_actions(ActionType.USE_NM, self.uroda_client, self.gameboard)
        mock.assert_not_called()

        # checks if using s2 works (heal ally down)
        self.uroda_healer.took_action = False
        self.move_controller.handle_actions(ActionType.USE_S2, self.uroda_client, self.gameboard)
        mock.assert_not_called()

        # the healer is the character that tried to act
        self.assertEqual(self.uroda_healer.special_points, 0)

    # Guard move testing
    # Tests guarding, damage when guarding (single attack and AOE), etc.
    def test_guard_bottom(self) -> None:
        # Should guard character in center, which is the healer
        self.uroda_attacker.took_action = True
        self.uroda_healer.took_action = True
        self.turpis_attacker.took_action = True
        self.turpis_healer.special_points = 10

        self.move_controller.handle_actions(ActionType.USE_NM, self.uroda_client, self.gameboard)

        # Test if they are now guarded
        self.assertEqual(self.uroda_healer.guardian, self.uroda_tank)

        # Deal AOE damage and test if it hits guarded and guardian
        self.move_controller.handle_actions(ActionType.USE_S1, self.turpis_client, self.gameboard)

        self.assertNotEqual(self.uroda_healer.current_health, self.uroda_healer.max_health)
        self.assertNotEqual(self.uroda_tank.current_health, self.uroda_tank.max_health)
        self.assertEqual(self.uroda_healer.guardian, self.uroda_tank)

        # Reset health and change took_actions
        self.uroda_healer.current_health = self.uroda_healer.max_health
        self.uroda_tank.current_health = self.uroda_tank.max_health
        self.turpis_attacker.took_action = False
        self.turpis_healer.took_action = True

        # Test guarding single damage to healer and guardian being set to None
        self.move_controller.handle_actions(ActionType.USE_NM, self.turpis_client, self.gameboard)

        self.assertEqual(self.uroda_healer.current_health, self.uroda_healer.max_health)
        self.assertNotEqual(self.uroda_tank.current_health, self.uroda_tank.max_health)
        self.assertEqual(self.uroda_healer.guardian, None)

    def test_guard_center(self) -> None:
        # Should guard both characters, top and bottom
        self.uroda_attacker.took_action = True
        self.uroda_healer.took_action = True
        self.turpis_attacker.took_action = True
        self.turpis_tank.took_action = True
        self.turpis_healer.special_points = 10

        # Swap uroda tank into center position
        self.swap_controller.handle_actions(ActionType.SWAP_UP, self.uroda_client, self.gameboard)

        # Test guard for allies
        self.uroda_tank.took_action = False
        self.move_controller.handle_actions(ActionType.USE_NM, self.uroda_client, self.gameboard)

        self.assertEqual(self.uroda_attacker.guardian, self.uroda_tank)
        self.assertEqual(self.uroda_healer.guardian, self.uroda_tank)

        # Deal AOE damage and test if it hits guarded and guardian
        self.move_controller.handle_actions(ActionType.USE_S1, self.turpis_client, self.gameboard)

        self.assertNotEqual(self.uroda_attacker.current_health, self.uroda_attacker.max_health)
        self.assertNotEqual(self.uroda_healer.current_health, self.uroda_healer.max_health)
        self.assertNotEqual(self.uroda_tank.current_health, self.uroda_tank.max_health)

        # Reset health and change took_actions
        self.uroda_attacker.current_health = self.uroda_attacker.max_health
        self.uroda_healer.current_health = self.uroda_healer.max_health
        self.uroda_tank.current_health = self.uroda_tank.max_health
        self.turpis_tank.took_action = False
        self.turpis_healer.took_action = True

        # Test guarding single damage to attacker, guardian set to None
        self.move_controller.handle_actions(ActionType.USE_S1, self.turpis_client, self.gameboard)

        self.assertEqual(self.uroda_attacker.current_health, self.uroda_attacker.max_health)
        self.assertNotEqual(self.uroda_tank.current_health, self.uroda_tank.max_health)
        self.assertEqual(self.uroda_attacker.guardian, None)
        self.assertEqual(self.uroda_healer.guardian, self.uroda_tank)

    # explicit move_logic tests below ---------------------------------------------------------------------

    def test_calculate_modifier_effect(self) -> None:
        # the turpis healer has speed 10; after debuff, the predicted value should be
        result: int = move_logic.calculate_modifier_effect(self.turpis_healer, self.attacker_moveset.get_s2())

        self.assertEqual(result, 7)

    def test_debuff_modifier_is_applied(self) -> None:
        # testing to ensure a debuff is applied properly from move_logic.py
        self.uroda_attacker.took_action = True

        # using the healer's debuff attack
        self.move_controller.handle_actions(ActionType.USE_S3, self.uroda_client, self.gameboard)

        # check that the turpis attacker's defense decreased
        self.assertEqual(self.turpis_attacker.defense.stage, -1)

        # ceiling(5 * 0.667) = 4
        self.assertEqual(self.turpis_attacker.defense.value, 4)
        self.assertEqual(self.turpis_attacker.defense.calculate_modifier(self.turpis_attacker.defense.stage), 0.667)

    def test_aoe_attack(self) -> None:
        # the uroda healer has the AOE, so set the attack to have taken their turn
        self.uroda_attacker.took_action = True

        # set all turpis characters to be on 1 HP
        self.turpis_attacker.current_health = 1
        self.turpis_tank.current_health = 1
        self.turpis_healer.current_health = 1

        self.move_controller.handle_actions(ActionType.USE_S1, self.uroda_client, self.gameboard)

        # check that all turpis characters have 0 HP
        self.assertEqual(self.turpis_attacker.current_health, 0)
        self.assertEqual(self.turpis_tank.current_health, 0)
        self.assertEqual(self.turpis_healer.current_health, 0)

    def test_attack_effect(self) -> None:
        # the uroda healer has the effects to test, so let it be its turn
        self.uroda_attacker.took_action = True

        self.move_controller.handle_actions(ActionType.USE_NM, self.uroda_client, self.gameboard)

        # the attack effect damages the user. 20 health - 10 damage = 10 remaining health
        self.assertEqual(self.uroda_healer.current_health, 10)

    def test_healing_effect(self) -> None:
        # the uroda healer has the effects to test, so let it be its turn
        self.uroda_attacker.took_action = True

        # set the allies' health to be 1 to test healing effect
        self.uroda_attacker.current_health = 1
        self.uroda_tank.current_health = 1

        self.move_controller.handle_actions(ActionType.USE_S1, self.uroda_client, self.gameboard)

        # the healing effect heals 10 health
        self.assertEqual(self.uroda_attacker.current_health, 11)
        self.assertEqual(self.uroda_tank.current_health, 11)

    def test_buff_effect(self) -> None:
        # the uroda healer has the effects to test, so let it be its turn
        self.uroda_attacker.took_action = True

        self.move_controller.handle_actions(ActionType.USE_S2, self.uroda_client, self.gameboard)

        # the buff effect boosts all opponents' speed stats by 1 stage
        self.assertEqual(self.turpis_attacker.speed.stage, 1)
        self.assertEqual(self.turpis_healer.speed.stage, 1)
        self.assertEqual(self.turpis_tank.speed.stage, 1)

    def test_debuff_effect(self) -> None:
        # the uroda healer has the effects to test, so let it be its turn
        self.uroda_attacker.took_action = True

        self.move_controller.handle_actions(ActionType.USE_S3, self.uroda_client, self.gameboard)

        # the debuff effect decreases all allies' speed stats by -1
        self.assertEqual(self.uroda_attacker.speed.stage, -1)
        self.assertEqual(self.uroda_healer.speed.stage, -1)
        self.assertEqual(self.uroda_tank.speed.stage, -1)
