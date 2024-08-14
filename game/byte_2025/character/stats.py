import math
from typing import Self

from game.common.enums import ObjectType
from game.common.game_object import GameObject
from game.config import STAGE_MAX, STAGE_MIN, MODIFIER_MAX, MODIFIER_MIN, NUMERATOR, DENOMINATOR


class Stat(GameObject):
    """
    The Stat class represents the different stats a character has: Attack, Defense, Speed.

    Each stat has a base value that is used as an initial value. The `value` property is the actual value that is used
    and modified for calculations.

    The `stage` property is used to help calculate the buff/debuff modifier that needs to be applied to a stat. The way
    this system works is similar to a slider or a number line. The bounds are from -4 to 4 inclusive. If the stage is
    at 0, that means the modifier is at x1. When the stage increases or decreases, the modifier is adjusted
    appropriately for the calculation.

    The AttackStat subclass will work a bit differently. The attack stat will simply be a modifier that is adjusted
    and affects the damage points of an attack Move when a character deals damage to an opponent. Therefore,
    the base value will always be 1 when initialized, and when the stage and modifier properties are calculated,
    the value will adjust appropriately as a modifier instead.

    Example:
        AttackStat value at stage +1 = 1.5
        AttackStat value at stage -1 = 0.667

    This is why the base_value and value properties are type hinted as int | float.
    """

    def __init__(self, base_value: int = 1):
        super().__init__()

        self.object_type = ObjectType.STAT
        self.base_value: int | float = base_value
        self.value: int | float = base_value
        self.stage: int = 0

    # override the hashable methods to easily compare stats
    def __gt__(self, other: Self | int) -> bool:
        if not isinstance(other, Stat | int):
            return False

        return self.value > other.value

    def __lt__(self, other: Self | int) -> bool:
        if not isinstance(other, Stat | int):
            return False

        return self.value < other.value

    def __ge__(self, other: Self | int) -> bool:
        if not isinstance(other, Stat | int):
            return False

        return self.value >= other.value

    def __le__(self, other: Self | int) -> bool:
        if not isinstance(other, Stat | int):
            return False

        return self.value <= other.value

    def __eq__(self, other: Self | int) -> bool:
        if not isinstance(other, Stat | int | int):
            return False

        # return the correct bool depending on if the 'other' value is another Stat or int; creates flexibility
        return self.value == other.value if isinstance(other, Stat) else self.value == other

    def __ne__(self, other: Self | int) -> bool:
        if not isinstance(other, Stat | int):
            return False

        return self.value != other.value

    @property
    def base_value(self) -> int | float:
        return self.__base_value

    @base_value.setter
    def base_value(self, base_value: int | float) -> None:
        if base_value is None or not isinstance(base_value, int | float):
            raise ValueError(f'{self.__class__.__name__}.base_value must be an int or float. It is a(n) '
                             f'{base_value.__class__.__name__} and has a value of {base_value}')

        if not base_value > 0:
            raise ValueError(f'{self.__class__.__name__}.base_value must be greater than 0')

        self.__base_value = base_value

    @property
    def value(self) -> int | float:
        return self.__value

    @value.setter
    def value(self, value: int | float) -> None:
        if value is None or not isinstance(value, int | float):
            raise ValueError(f'{self.__class__.__name__}.value must be an int or float. It is a(n) '
                             f'{value.__class__.__name__} and has a value of {value}')

        if value < 0:
            raise ValueError(f'{self.__class__.__name__}.value must be a positive int or float')

        self.__value = value

    @property
    def stage(self) -> int:
        return self.__stage

    @stage.setter
    def stage(self, stage: int) -> None:
        if stage is None or not isinstance(stage, int):
            raise ValueError(f'{self.__class__.__name__}.stage must be an int. It is a(n) '
                             f'{stage.__class__.__name__} and has a value of {stage}')

        if stage < STAGE_MIN or stage > STAGE_MAX:
            raise ValueError(
                f'{self.__class__.__name__}.stage must be between {STAGE_MIN} and {STAGE_MAX} inclusive. '
                f'The value given was {stage}')

        self.__stage = stage

    def is_maxed(self) -> bool:
        """
        Returns true if the stat is maxed out. This is determined by how many stages the stat has been increased by.
        A stat is maxed out if at +4.
        """
        return self.stage == STAGE_MAX

    def is_minimized(self) -> bool:
        """
        Returns true if the stat is minimized. This is determined by how many stages the stat has been decreased by.
        A stat is minimized if at self.__min.
        """
        return self.stage == STAGE_MIN

    def calculate_stage_update(self, stages: int = 0) -> int:
        """
        Given the amount of stages to increase or decrease the stats stages, it will return what the stat's stage
        will be example to.
        """

        # the following cleanly calculates what the stage value will be using value comparisons without if statements
        # gets the largest value that is still in range of the value of STAGE_MAX
        max_calc: int = min(STAGE_MAX, self.stage + stages)

        # gets the smallest value that is still in range of the value of STAGE_MIN
        min_calc: int = min(STAGE_MIN, self.stage - stages)

        # by comparing which of the two values is largest, the correctly adjusted value is returned
        return max(min_calc, max_calc)

    def calculate_modifier(self, stage: int) -> float:
        """
        Calculates the stat's potential modifier by adjusting a fraction based on the stage.

        Formulas:
            * (numerator + stage) / denominator if stage is positive
            * numerator / (denominator + stage) if stage is negative

        This allows for the stat's value to appropriately scale in both directions.

        With the current settings:

            =========== =================== ==================
            Stage State Fraction Multiplier Decimal Multiplier
            =========== =================== ==================
                -4           2/6 (1/3)             0.333

                -3              2/5                 0.4

                -2           2/4 (1/2)              0.5

                -1              2/3                0.667

                 0               1                   1

                 1              3/2                 1.5

                 2            4/2 (2)                2

                 3              5/2                 2.5

                 4            6/2 (3)                3
            =========== =================== ==================
        """

        numerator: int = NUMERATOR
        denominator: int = DENOMINATOR

        # if the stage is positive, add its value to the numerator; else, add to denominator
        if stage > 0:
            numerator += stage
        else:
            # need to use the absolute value of the negative int
            denominator += abs(stage)

        # round the decimal to 3 decimal places
        return round(numerator / denominator, 3)

    def get_and_apply_modifier(self, stages: int = 0):
        self.stage = self.calculate_stage_update(stages)
        modifier: float = self.calculate_modifier(self.stage)

        # if the stat being modified is the attack stat, its value should always equal is modifier
        # otherwise, if any other stat, calculate the new value by using the ceiling function
        # always multiply the base value and modifier to easily calculate the correct result without additional rounding
        self.value = self.base_value * modifier if isinstance(self, AttackStat) \
            else math.ceil(self.base_value * modifier)

    def to_json(self) -> dict:
        data: dict = super().to_json()
        data['base_value'] = self.base_value
        data['value'] = self.value
        data['stage'] = self.stage

        return data

    def from_json(self, data: dict) -> Self:
        super().from_json(data)
        self.base_value = data['base_value']
        self.value = data['value']
        self.stage = data['stage']

        return self


class AttackStat(Stat):
    def __init__(self):
        super().__init__(1)
        self.object_type = ObjectType.ATTACK_STAT


class DefenseStat(Stat):
    def __init__(self, base_value: int = 1):
        super().__init__(base_value)
        self.object_type = ObjectType.DEFENSE_STAT


class SpeedStat(Stat):
    def __init__(self, base_value: int = 1):
        super().__init__(base_value)
        self.object_type = ObjectType.SPEED_STAT
