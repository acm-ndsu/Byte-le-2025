import unittest

from game.byte_2025.character.stat import Stat
from game.config import STAGE_MAX, STAGE_MIN, MODIFIER_MAX, MODIFIER_MIN


class TestStat(unittest.TestCase):
    def setUp(self):
        self.stat = Stat(5)
        self.string: str = 'hi'
        self.min: int = -5
        self.max: int = 5
        self.min_float: float = 0.0
        self.max_float: float = 2.1

    def test_properties(self):
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
        self.assertEqual(str(e.exception), f'{self.stat.__class__.__name__}.base_value must be a positive int')

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
            self.stat.stage = self.min
        self.assertEqual(str(e.exception), f'{self.stat.__class__.__name__}.stage must be between {STAGE_MIN} and '
                                           f'{STAGE_MAX} inclusive. The value given was {self.min}')

        with self.assertRaises(ValueError) as e:
            self.stat.stage = self.max
        self.assertEqual(str(e.exception), f'{self.stat.__class__.__name__}.stage must be between {STAGE_MIN} '
                                           f'and {STAGE_MAX} inclusive. The value given was {self.max}')

        with self.assertRaises(ValueError) as e:
            self.stat.modifier = self.string
        self.assertEqual(str(e.exception), f'{self.stat.__class__.__name__}.modifier must be a float. It is a(n) '
                                           f'{self.string.__class__.__name__} and has a value of {self.string}')

        with self.assertRaises(ValueError) as e:
            self.stat.modifier = self.min_float
        self.assertEqual(str(e.exception), f'{self.stat.__class__.__name__}.modifier must be between '
                                           f'{MODIFIER_MIN} exclusive and {MODIFIER_MAX} inclusive. The value given '
                                           f'was {self.min_float}')
