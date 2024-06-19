import unittest
from game.common.enums import *
from game.byte_2025.move import *
import game.test_suite.utils



class TestMove(unittest.TestCase):
    """
        `Test Move Notes:`

            This class tests the different methods in the Move class.
        """

    def setUp(self) -> None:
        self.move: Move = Move()
        self.attack: Attack = Attack(name="Basic", damage_points=1)
        self.HEAL: Heal = HEAL(move)
        self.DEBUFF: Debuff = DEBUFF(move)
        self.BUFF: Buff = BUFF(move)
        self.utils = game.test_suite.utils

    def test_heal(self)-> None:
        self.Heal = 5.5
        self.assertEqual(self.move.HEAL, 5.5)

    def test_attack(self)-> None:
        self.Attack = 5
        self.assertEqual(self.move.ATTACK, 5)


    def test_buff(self) -> None:
        self.Buff = 5.5
        self.assertEqual(self.move.move_type.BUFF(buff))

    def test_debuff(self) -> None:
        self.Debuff = 5.5
        self.assertEqual(self.move.DEBUFF, 5.5)