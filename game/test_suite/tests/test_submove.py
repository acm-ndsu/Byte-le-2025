import unittest

from game.byte_2025.moves.submove import Submove
from game.common.enums import TargetType, MoveType


class TestSubmove(unittest.TestCase):
    def setUp(self) -> None:
        self.submove: Submove = Submove()

    def test_no_submove_can_be_set(self):
        with self.assertRaises(ValueError) as e:
            self.submove.submove = Submove(TargetType.SINGLE_OPP, MoveType.DEBUFF)
        self.assertEqual(e.exception, f'Submove cannot have a submove object assigned to it.')
