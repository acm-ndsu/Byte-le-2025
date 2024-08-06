import unittest

from game.byte_2025.moves.moves import *
from game.byte_2025.moves.moveset import Moveset


class TestMoveset(unittest.TestCase):
    def setUp(self):
        self.na: Attack = Attack('Normal Attack')
        self.s1: Buff = Buff('Special 1')
        self.s2: Debuff = Debuff('Special 2')
        self.s3: Heal = Heal('Special 3')
        self.moveset = Moveset((self.na, self.s1, self.s2, self.s3))

    def test_get_na(self):
        self.assertEqual(self.moveset.get_na(), self.na)

    def test_get_s1(self):
        self.assertEqual(self.moveset.get_s1(), self.s1)

    def test_get_s2(self):
        self.assertEqual(self.moveset.get_s2(), self.s2)

    def test_get_s3(self):
        self.assertEqual(self.moveset.get_s3(), self.s3)

    def test_json(self):
        data: dict = self.moveset.to_json()
        other_moveset: Moveset = Moveset().from_json(data)

        self.assertEqual(['NA', 'S1', 'S2', 'S3'], list(self.moveset.moves.keys()))

        for move, other_move in zip(self.moveset.moves.values(), other_moveset.moves.values()):
            self.assertEqual(move.object_type, other_move.object_type)
            self.assertEqual(move.name, other_move.name)
            self.assertEqual(move.target_type, other_move.target_type)
            self.assertEqual(move.move_type, other_move.move_type)
            self.assertEqual(move.cost, other_move.cost)
            self.assertEqual(move.effect, other_move.effect)

