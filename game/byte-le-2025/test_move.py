import unittest
from game.common.enums import *
from game.common.enums import *
from move import *
import game.test_suite.utils



class TestMove(unittest.TestCase):


    def setUp(self) -> None:
        self.move: Move = Move()
        self.utils = game.test_suite.utils

    def testHeal(self)-> None:
        heal_points = 5.5
        self.assertEqual(self.move.HEAL, 5.5)

    def testAttack(self)-> None:
        attack = 5
        self.assertEqual(self.move.ATTACK, 5)


    def testBuff(self) -> None:
        buff = 5.5
        self.assertEqual(self.move.move_type.BUFF(buff))

    def testDebuff(self) -> None:
        debuff = 5.5
        self.assertEqual(self.move.DEBUFF, 5.5)