import unittest

from game.byte_2025.character.stats import *
from game.config import STAGE_MAX, STAGE_MIN, MODIFIER_MAX, MODIFIER_MIN


class TestStat(unittest.TestCase):
    def setUp(self):
        self.stat = Stat(5)
        self.other_stat = Stat(1)
        self.attack_stat = AttackStat()
        self.defense_stat = DefenseStat(5)
        self.speed_stat = SpeedStat(5)
        self.string: str = 'hi'
        self.stage_min: int = STAGE_MIN - 1
        self.stage_max: int = STAGE_MAX + 1
        self.modifier_min: float = 0.0
        self.modifier_max: float = MODIFIER_MAX + 1

    def test_overridden_hash_methods(self) -> None:
        self.assertNotEqual(self.stat, self.other_stat)
        self.assertGreater(self.stat, self.other_stat)
        self.assertLess(self.other_stat, self.stat)

        self.other_stat.value = 5

        self.assertGreaterEqual(self.stat, self.other_stat)
        self.assertLessEqual(self.stat, self.other_stat)
        self.assertEqual(self.stat, self.other_stat)

        # test failing cases for the hashable methods
        self.assertFalse(self.stat == 'hi')
        self.assertFalse(self.stat < 'hi')
        self.assertFalse(self.stat > 'hi')
        self.assertFalse(self.stat <= 'hi')
        self.assertFalse(self.stat >= 'hi')
        self.assertFalse(self.stat != 'hi')

    def test_properties(self) -> None:
        self.assertEqual(self.stat.base_value, 5)
        self.assertEqual(self.stat.value, 5)
        self.assertEqual(self.stat.stage, 0)

        # testing base_value
        with self.assertRaises(ValueError) as e:
            self.stat.base_value = self.string
        self.assertEqual(str(e.exception),
                         f'{self.stat.__class__.__name__}.base_value must be an int or float. It is a(n) '
                         f'{self.string.__class__.__name__} and has a value of {self.string}')

        with self.assertRaises(ValueError) as e:
            self.stat.base_value = -1
        self.assertEqual(str(e.exception), f'{self.stat.__class__.__name__}.base_value must be greater than 0')

        # testing value
        with self.assertRaises(ValueError) as e:
            self.stat.value = self.string
        self.assertEqual(str(e.exception), f'{self.stat.__class__.__name__}.value must be an int or float. It is a(n) '
                                           f'{self.string.__class__.__name__} and has a value of {self.string}')

        with self.assertRaises(ValueError) as e:
            self.stat.value = -1
        self.assertEqual(str(e.exception), f'{self.stat.__class__.__name__}.value must be a positive int or float')

        # testing stage
        with self.assertRaises(ValueError) as e:
            self.stat.stage = self.string
        self.assertEqual(str(e.exception), f'{self.stat.__class__.__name__}.stage must be an int. It is a(n) '
                                           f'{self.string.__class__.__name__} and has a value of {self.string}')

        with self.assertRaises(ValueError) as e:
            self.stat.stage = self.stage_min
        self.assertEqual(str(e.exception), f'{self.stat.__class__.__name__}.stage must be between {STAGE_MIN} and '
                                           f'{STAGE_MAX} inclusive. The value given was {self.stage_min}')

        with self.assertRaises(ValueError) as e:
            self.stat.stage = self.stage_max
        self.assertEqual(str(e.exception), f'{self.stat.__class__.__name__}.stage must be between {STAGE_MIN} '
                                           f'and {STAGE_MAX} inclusive. The value given was {self.stage_max}')

    def test_is_maxed(self) -> None:
        # should not be maxed after initialization
        self.assertFalse(self.stat.is_maxed())

        self.stat.stage = STAGE_MAX
        self.assertTrue(self.stat.is_maxed)

    def test_is_minimized(self) -> None:
        # should not be minimized after initialization
        self.assertFalse(self.stat.is_minimized())

        self.stat.stage = STAGE_MIN
        self.assertTrue(self.stat.is_minimized())

    def test_calculate_stage_update_from_stage_0(self) -> None:
        # max the stat
        stage: int = self.stat.calculate_stage_update(STAGE_MAX)
        self.assertEqual(stage, STAGE_MAX)

        # set the stat back to neutral (stage 0)
        self.stat.stage = 0

        # minimize the stat
        stage = self.stat.calculate_stage_update(STAGE_MIN)
        self.assertEqual(stage, STAGE_MIN)

    def test_calculate_stage_update_not_going_past_bounds(self) -> None:
        # set the stage to 2
        self.stat.stage = 2

        # check that adding a value > 2 leaves the stage at +4
        stage: int = self.stat.calculate_stage_update(STAGE_MAX)
        self.assertEqual(stage, STAGE_MAX)

        # set the stage to -2
        self.stat.stage = -2

        # check that adding a value < -2 leaves the stage at -4
        stage = self.stat.calculate_stage_update(STAGE_MIN)
        self.assertEqual(stage, STAGE_MIN)

    def test_calculate_stage_update_passed_in_0(self):
        stage: int = self.stat.calculate_stage_update(0)
        self.assertEqual(stage, 0)

    def test_calculate_stage_update_mid_range_values(self) -> None:
        # update from 0 -> 3
        stage: int = self.stat.calculate_stage_update(3)
        self.stat.stage = stage
        self.assertEqual(stage, 3)

        # update from 3 -> -2
        stage = self.stat.calculate_stage_update(-5)
        self.stat.stage = stage
        self.assertEqual(stage, -2)

        # update from -2 -> 0
        stage = self.stat.calculate_stage_update(2)
        self.stat.stage = stage
        self.assertEqual(stage, 0)

    def test_get_and_apply_modifier(self) -> None:
        # at stage 3 (modifier = 2.5), the stat's value will become 13 due to ceiling function
        self.stat.apply_modifier(3)
        self.assertEqual(self.stat.calculate_modifier(self.stat.stage), 2.5)
        self.assertEqual(self.stat.value, 13)

        # at stage 4 (modifier = 3.0), the stat's value will become 15
        self.stat.apply_modifier(1)  # use +1 since it's at +3 already
        self.assertEqual(self.stat.calculate_modifier(self.stat.stage), 3.0)
        self.assertEqual(self.stat.value, 15)

        # at stage -4 (modifier = 0.333), the stat's value will become 2 due to ceiling function
        self.stat.apply_modifier(-8)  # use -8 since it's at +4 already
        self.assertEqual(self.stat.calculate_modifier(self.stat.stage), 0.333)
        self.assertEqual(self.stat.value, 2)

        # at stage -3 (modifier 0.4), the stat's value will become 2 still
        self.stat.apply_modifier(1)  # use +1 since it's at -4 already
        self.assertEqual(self.stat.calculate_modifier(self.stat.stage), 0.4)
        self.assertEqual(self.stat.value, 2)

    def test_attack_defense_and_speed_stats(self):
        self.assertEqual(self.attack_stat.object_type, ObjectType.ATTACK_STAT)
        self.assertEqual(self.attack_stat.base_value, 1)
        self.assertEqual(self.attack_stat.value, 1)

        self.assertEqual(self.defense_stat.object_type, ObjectType.DEFENSE_STAT)
        self.assertEqual(self.defense_stat.base_value, 5)
        self.assertEqual(self.defense_stat.value, 5)

        self.assertEqual(self.speed_stat.object_type, ObjectType.SPEED_STAT)
        self.assertEqual(self.speed_stat.base_value, 5)
        self.assertEqual(self.speed_stat.value, 5)

        # check the overridden hashable == operator still works
        self.assertEqual(self.defense_stat, self.speed_stat)

    # the value and modifier must be equal
    def test_modifying_attack(self):
        # check stage 3
        self.attack_stat.apply_modifier(3)

        # a = b = c; the value must equal the modifier, and the modifier must equal 2.5
        self.assertEqual(self.attack_stat.value, 2.5)
        self.assertEqual(self.attack_stat.calculate_modifier(self.attack_stat.stage), 2.5)

        # check stage 4
        self.attack_stat.apply_modifier(1)
        self.assertEqual(self.attack_stat.value, 3)
        self.assertEqual(self.attack_stat.calculate_modifier(self.attack_stat.stage), 3)

        # check stage -2
        self.attack_stat.apply_modifier(-6)
        self.assertEqual(self.attack_stat.value, 0.5)
        self.assertEqual(self.attack_stat.calculate_modifier(self.attack_stat.stage), 0.5)

        # check going back to stage 0
        self.attack_stat.apply_modifier(2)
        self.assertEqual(self.attack_stat.value, 1)
        self.assertEqual(self.attack_stat.calculate_modifier(self.attack_stat.stage), 1)

    def test_json(self) -> None:
        data: dict = self.stat.to_json()
        stat: Stat = Stat().from_json(data)
        self.assertEqual(stat.object_type, self.stat.object_type)
        self.assertEqual(stat.base_value, self.stat.base_value)
        self.assertEqual(stat.value, self.stat.value)
        self.assertEqual(stat.stage, self.stat.stage)

        data = self.attack_stat.to_json()
        attack_stat: AttackStat = AttackStat().from_json(data)
        self.assertEqual(attack_stat.object_type, self.attack_stat.object_type)
        self.assertEqual(attack_stat.base_value, self.attack_stat.base_value)
        self.assertEqual(attack_stat.value, self.attack_stat.value)
        self.assertEqual(attack_stat.stage, self.attack_stat.stage)

        data = self.defense_stat.to_json()
        defense_stat: DefenseStat = DefenseStat().from_json(data)
        self.assertEqual(defense_stat.object_type, self.defense_stat.object_type)
        self.assertEqual(defense_stat.base_value, self.defense_stat.base_value)
        self.assertEqual(defense_stat.value, self.defense_stat.value)
        self.assertEqual(defense_stat.stage, self.defense_stat.stage)

        data = self.speed_stat.to_json()
        speed_stat: SpeedStat = SpeedStat().from_json(data)
        self.assertEqual(speed_stat.object_type, self.speed_stat.object_type)
        self.assertEqual(speed_stat.base_value, self.speed_stat.base_value)
        self.assertEqual(speed_stat.value, self.speed_stat.value)
        self.assertEqual(speed_stat.stage, self.speed_stat.stage)
