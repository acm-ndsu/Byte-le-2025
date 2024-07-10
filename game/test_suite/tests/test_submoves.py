import unittest

from game.byte_2025.moves.submoves import *
from game.common.enums import *


class TestSubmoves(unittest.TestCase):
    """
    `Test Move Notes:`

    This class tests the different classes of the submoves module.
    This class tests the constructors, getters, setters, and json methods.
    """
    # TEST THE USE METHOD ONCE IMPLEMENTED
    def setUp(self):
        self.submove: Submove = Submove()
        self.subattack: AttackSubmove = AttackSubmove(target_type=TargetType.SINGLE_OPP, damage_points=10)
        self.subheal: HealSubmove = HealSubmove(target_type=TargetType.ALL_ALLY, heal_points=5)
        self.subbuff: BuffSubmove = BuffSubmove(target_type=TargetType.SINGLE_ALLY, buff_amount=5)
        self.subdebuff: DebuffSubmove = DebuffSubmove(target_type=TargetType.SINGLE_OPP, debuff_amount=10)

    def test_base_init(self) -> None:
        self.assertEqual(self.submove.object_type, ObjectType.SUBMOVE)
        self.assertEqual(self.submove.move_type, MoveType.MOVE)
        self.assertEqual(self.submove.target_type, TargetType.SELF)

    def test_base_json(self) -> None:
        data: dict = self.submove.to_json()
        submove: Submove = Submove().from_json(data)
        self.assertEqual(submove.object_type, self.submove.object_type)

    def test_subattack_json(self) -> None:
        data: dict = self.subattack.to_json()
        subattack: AttackSubmove = AttackSubmove().from_json(data)
        self.assertEqual(subattack.object_type, self.subattack.object_type)
        self.assertEqual(subattack.damage_points, self.subattack.damage_points)

    def test_subheal_json(self) -> None:
        data: dict = self.subheal.to_json()
        subheal: HealSubmove = HealSubmove().from_json(data)
        self.assertEqual(subheal.object_type, self.subheal.object_type)
        self.assertEqual(subheal.heal_points, self.subheal.heal_points)

    def test_subbuff_json(self) -> None:
        data: dict = self.subbuff.to_json()
        subbuff: BuffSubmove = BuffSubmove().from_json(data)
        self.assertEqual(subbuff.object_type, self.subbuff.object_type)
        self.assertEqual(subbuff.buff_amount, self.subbuff.buff_amount)

    def test_subdebuff_json(self) -> None:
        data: dict = self.subdebuff.to_json()
        subdebuff: DebuffSubmove = DebuffSubmove().from_json(data)
        self.assertEqual(subdebuff.object_type, self.subdebuff.object_type)
        self.assertEqual(subdebuff.debuff_amount, self.subdebuff.debuff_amount)




