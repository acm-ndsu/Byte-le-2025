import unittest

from game.byte_2025.character.stat import Stat
from game.config import STAGE_MAX, STAGE_MIN, MODIFIER_MAX, MODIFIER_MIN


class TestStat(unittest.TestCase):
    def setUp(self):
        self.stat = Stat(5)
        self.other_stat = Stat(1)
        self.string: str = 'hi'
        self.stage_min: int = STAGE_MIN - 1
        self.max: int = STAGE_MAX + 1
        self.modifier_min: float = 0.0
        self.modifier_max: float = 2.1

    def test_overridden_hash_methods(self) -> None:
        self.assertNotEqual(self.stat, self.other_stat)
        self.assertGreater(self.stat, self.other_stat)
        self.assertLess(self.other_stat, self.stat)

        self.other_stat.value = 5

        self.assertGreaterEqual(self.stat, self.other_stat)
        self.assertLessEqual(self.stat, self.other_stat)
        self.assertEqual(self.stat, self.other_stat)

    def test_properties(self) -> None:
        self.assertEqual(self.stat.base_value, 5)
        self.assertEqual(self.stat.value, 5)
        self.assertEqual(self.stat.stage, 0)
        self.assertEqual(self.stat.modifier, 1.0)

        # testing base_value
        with self.assertRaises(ValueError) as e:
            self.stat.base_value = self.string
        self.assertEqual(str(e.exception), f'{self.stat.__class__.__name__}.base_value must be an int. It is a(n) '
                                           f'{self.string.__class__.__name__} and has a value of {self.string}')

        with self.assertRaises(ValueError) as e:
            self.stat.base_value = -1
        self.assertEqual(str(e.exception), f'{self.stat.__class__.__name__}.base_value must be greater than 0')

        # testing value
        with self.assertRaises(ValueError) as e:
            self.stat.value = self.string
        self.assertEqual(str(e.exception), f'{self.stat.__class__.__name__}.value must be an int. It is a(n) '
                                           f'{self.string.__class__.__name__} and has a value of {self.string}')

        with self.assertRaises(ValueError) as e:
            self.stat.value = -1
        self.assertEqual(str(e.exception), f'{self.stat.__class__.__name__}.value must be a positive int')

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
            self.stat.stage = self.max
        self.assertEqual(str(e.exception), f'{self.stat.__class__.__name__}.stage must be between {STAGE_MIN} '
                                           f'and {STAGE_MAX} inclusive. The value given was {self.max}')

        with self.assertRaises(ValueError) as e:
            self.stat.modifier = self.string
        self.assertEqual(str(e.exception), f'{self.stat.__class__.__name__}.modifier must be a float. It is a(n) '
                                           f'{self.string.__class__.__name__} and has a value of {self.string}')

        with self.assertRaises(ValueError) as e:
            self.stat.modifier = self.modifier_min
        self.assertEqual(str(e.exception), f'{self.stat.__class__.__name__}.modifier must be between '
                                           f'{MODIFIER_MIN} exclusive and {MODIFIER_MAX} inclusive. The value given '
                                           f'was {self.modifier_min}')

    def test_is_maxed(self) -> None:
        self.assertFalse(self.stat.is_maxed())

        self.stat.stage = STAGE_MAX
        self.assertTrue(self.stat.is_maxed)

    def test_is_minimized(self) -> None:
        self.assertFalse(self.stat.is_minimized())

        self.stat.stage = STAGE_MIN
        self.assertTrue(self.stat.is_minimized())

    def test_get_stage_update_from_stage_0(self) -> None:
        # max the stat
        stage: int = self.stat.get_stage_update(STAGE_MAX)
        self.assertEqual(stage, STAGE_MAX)

        # set the stat back to neutral (stage 0)
        self.stat.stage = 0

        # minimize the stat
        stage = self.stat.get_stage_update(STAGE_MIN)
        self.assertEqual(stage, STAGE_MIN)

    def test_get_stage_update_not_going_over_cap(self) -> None:
        # set the stage to 2
        self.stat.stage = 2

        # check that adding a value > 2 leaves the stage at +4
        stage: int = self.stat.get_stage_update(STAGE_MAX)
        self.assertEqual(stage, STAGE_MAX)

        # set the stage to -2
        self.stat.stage = -2

        # check that adding a value < -2 leaves the stage at -4
        stage = self.stat.get_stage_update(STAGE_MIN)
        self.assertEqual(stage, STAGE_MIN)

    def test_get_stage_update_passed_in_0(self):
        stage: int = self.stat.get_stage_update(0)
        self.assertEqual(stage, 0)

    def test_get_stage_update_mid_range_values(self) -> None:
        # update from 0 -> 3
        stage: int = self.stat.get_stage_update(3)
        self.stat.stage = stage
        self.assertEqual(stage, 3)

        # update from 3 -> -2
        stage = self.stat.get_stage_update(-5)
        self.stat.stage = stage
        self.assertEqual(stage, -2)

        # update from -2 to 0
        stage = self.stat.get_stage_update(2)
        self.stat.stage = stage
        self.assertEqual(stage, 0)

    def test_get_and_apply_modifier(self) -> None:
        # at stage 3 (modifier = 2.5), the stat's value will become 13 due to ceiling function
        self.stat.get_and_apply_modifier(3)
        self.assertEqual(self.stat.modifier, 2.5)
        self.assertEqual(self.stat.value, 13)

        # at stage 4 (modifier = 3.0), the stat's value will become 15
        self.stat.get_and_apply_modifier(1)  # use +1 since it's at +3 already
        self.assertEqual(self.stat.modifier, 3.0)
        self.assertEqual(self.stat.value, 15)

        # at stage -4 (modifier = 0.333), the stat's value will become 2 due to ceiling function
        self.stat.get_and_apply_modifier(-8)  # use -8 since it's at +4 already
        self.assertEqual(self.stat.modifier, 0.333)
        self.assertEqual(self.stat.value, 2)

        # at stage -3 (modifier 0.4), the stat's value will become 2 still
        self.stat.get_and_apply_modifier(1)  # use +1 since it's at -4 already
        self.assertEqual(self.stat.modifier, 0.4)
        self.assertEqual(self.stat.value, 2)

    def test_json(self) -> None:
        data: dict = self.stat.to_json()
        stat: Stat = Stat().from_json(data)
        self.assertEqual(stat.object_type, self.stat.object_type)
        self.assertEqual(stat.base_value, self.stat.base_value)
        self.assertEqual(stat.value, self.stat.value)
        self.assertEqual(stat.stage, self.stat.stage)
        self.assertEqual(stat.modifier, self.stat.modifier)
