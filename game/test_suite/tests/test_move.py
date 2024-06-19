import unittest
from game.common.enums import *
from game.byte_2025.move import *
from game.test_suite.utils import spell_check


class TestMove(unittest.TestCase):
    """
    `Test Move Notes:`

        This class tests the different methods in the Move class.
    """

    def setUp(self) -> None:
        self.move: Move = Move()
        self.attack: Attack = Attack(name="Basic Attack", damage_points=1)
        self.heal: Heal = Heal(name="Basic Heal", heal_points=1)
        self.buff: Buff = Buff('Big Buff', target_type=TargetType.ALL_ALLY, buff_amount=2, subaction=self.attack)
        self.debuff: Debuff = Debuff(name="Big Debuff", cost=2, debuff_amount=2)

    def test_attack_init(self) -> None:
        self.assertEqual(self.attack.name, "Basic Attack")
        self.assertEqual(self.attack.move_type, MoveType.ATTACK)
        self.assertEqual(self.attack.target_type, TargetType.SINGLE_OPP)
        self.assertEqual(self.attack.cost, 0)
        self.assertEqual(self.attack.subaction, None)
        self.assertEqual(self.attack.damage_points, 1)

    def test_heal_init(self) -> None:
        self.assertEqual(self.heal.name, "Basic Heal")
        self.assertEqual(self.heal.move_type, MoveType.HEAL)
        self.assertEqual(self.heal.target_type, TargetType.SINGLE_ALLY)
        self.assertEqual(self.heal.cost, 0)
        self.assertEqual(self.heal.subaction, None)
        self.assertEqual(self.heal.heal_points, 1)

    def test_buff_init(self) -> None:
        self.assertEqual(self.buff.name, "Big Buff")
        self.assertEqual(self.buff.move_type, MoveType.BUFF)
        self.assertEqual(self.buff.target_type, TargetType.ALL_ALLY)
        self.assertEqual(self.buff.cost, 0)
        self.assertEqual(self.buff.subaction, self.attack)
        self.assertEqual(self.buff.buff_amount, 2)

    def test_debuff_init(self) -> None:
        self.assertEqual(self.debuff.name, "Big Debuff")
        self.assertEqual(self.debuff.move_type, MoveType.DEBUFF)
        self.assertEqual(self.debuff.target_type, TargetType.SINGLE_OPP)
        self.assertEqual(self.debuff.cost, 2)
        self.assertEqual(self.debuff.subaction, None)
        self.assertEqual(self.debuff.debuff_amount, 2)
