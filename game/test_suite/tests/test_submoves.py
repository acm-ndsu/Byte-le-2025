import unittest

from game.byte_2025.moves.effect import *
from game.common.enums import *


class TestEffects(unittest.TestCase):
    """
    `Test Move Notes:`

    This class tests the different classes of the effects module.
    This class tests the constructors, getters, setters, and json methods.
    """
    # TEST THE USE METHOD ONCE IMPLEMENTED
    def setUp(self):
        self.effect: Effect = Effect()
        self.attack_effect: AttackEffect = AttackEffect(target_type=TargetType.SINGLE_OPP, damage_points=10)
        self.heal_effect: HealEffect = HealEffect(target_type=TargetType.ALL_ALLY, heal_points=5)
        self.buff_effect: BuffEffect = BuffEffect(target_type=TargetType.SINGLE_ALLY, buff_amount=5)
        self.debuff_effect: DebuffEffect = DebuffEffect(target_type=TargetType.SINGLE_OPP, debuff_amount=10)

    def test_base_init(self) -> None:
        self.assertEqual(self.effect.object_type, ObjectType.EFFECT)
        self.assertEqual(self.effect.move_type, MoveType.MOVE)
        self.assertEqual(self.effect.target_type, TargetType.SELF)

    def test_base_json(self) -> None:
        data: dict = self.effect.to_json()
        effect: Effect = Effect().from_json(data)
        self.assertEqual(effect.object_type, self.effect.object_type)

    def test_subattack_json(self) -> None:
        data: dict = self.attack_effect.to_json()
        subattack: AttackEffect = AttackEffect().from_json(data)
        self.assertEqual(subattack.object_type, self.attack_effect.object_type)
        self.assertEqual(subattack.damage_points, self.attack_effect.damage_points)

    def test_subheal_json(self) -> None:
        data: dict = self.heal_effect.to_json()
        subheal: HealEffect = HealEffect().from_json(data)
        self.assertEqual(subheal.object_type, self.heal_effect.object_type)
        self.assertEqual(subheal.heal_points, self.heal_effect.heal_points)

    def test_subbuff_json(self) -> None:
        data: dict = self.buff_effect.to_json()
        subbuff: BuffEffect = BuffEffect().from_json(data)
        self.assertEqual(subbuff.object_type, self.buff_effect.object_type)
        self.assertEqual(subbuff.buff_amount, self.buff_effect.buff_amount)

    def test_subdebuff_json(self) -> None:
        data: dict = self.debuff_effect.to_json()
        subdebuff: DebuffEffect = DebuffEffect().from_json(data)
        self.assertEqual(subdebuff.object_type, self.debuff_effect.object_type)
        self.assertEqual(subdebuff.debuff_amount, self.debuff_effect.debuff_amount)




