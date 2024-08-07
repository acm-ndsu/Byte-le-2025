from typing import Self

from game.common.enums import ObjectType
from game.common.game_object import GameObject
from game.config import STAGE_MAX, STAGE_MIN, MODIFIER_MAX, MODIFIER_MIN


class Stat(GameObject):
    def __init__(self, base_value: int):
        super().__init__()

        self.object_type = ObjectType.STAT
        self.base_value = base_value
        self.value = base_value
        self.stage: int = 0
        self.modifier: float = 1.0

    # override the hashable methods to easily compare stats
    def __gt__(self, other: Self) -> bool:
        if not isinstance(other, Stat):
            return False

        return self.value > other.value

    def __lt__(self, other: Self) -> bool:
        if not isinstance(other, Stat):
            return False

        return self.value < other.value

    def __ge__(self, other: Self) -> bool:
        if not isinstance(other, Stat):
            return False

        return self.value >= other.value

    def __le__(self, other: Self) -> bool:
        if not isinstance(other, Stat):
            return False

        return self.value <= other.value

    def __eq__(self, other: Self) -> bool:
        if not isinstance(other, Stat):
            return False

        return self.value == other.value

    def __ne__(self, other: Self) -> bool:
        if not isinstance(other, Stat):
            return False

        return self.value != other.value

    @property
    def base_value(self) -> int:
        return self.__base_value

    @base_value.setter
    def base_value(self, base_value: int) -> None:
        if base_value is None or not isinstance(base_value, int):
            raise ValueError(f'{self.__class__.__name__}.base_value must be an int. It is a(n) '
                             f'{base_value.__class__.__name__} and has a value of {base_value}')

        if base_value < 0:
            raise ValueError(f'{self.__class__.__name__}.base_value must be a positive int')

        self.__base_value = base_value

    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int) -> None:
        if value is None or not isinstance(value, int):
            raise ValueError(f'{self.__class__.__name__}.value must be an int. It is a(n) '
                             f'{value.__class__.__name__} and has a value of {value}')

        if value < 0:
            raise ValueError(f'{self.__class__.__name__}.value must be a positive int')

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

    @property
    def modifier(self) -> float:
        return self.__modifier

    @modifier.setter
    def modifier(self, modifier: float) -> None:
        if modifier is None or not isinstance(modifier, float):
            raise ValueError(f'{self.__class__.__name__}.modifier must be a float. It is a(n) '
                             f'{modifier.__class__.__name__} and has a value of {modifier}')

        if modifier < MODIFIER_MIN or modifier > MODIFIER_MAX:
            raise ValueError(f'{self.__class__.__name__}.modifier must be between {MODIFIER_MIN} exclusive and '
                             f'{MODIFIER_MAX} inclusive. The value given was {modifier}')

        self.__modifier = modifier

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

    def update_stage(self, stages: int) -> None:
        """
        Given the amount of stages to increase or decrease the stats stages, it will update the stats stages.

        Note: if the stat is at +3 and the given stages to increase by is +2, it will cap at +4. The same applies
        for the stat at -4.
        """

        # the following cleanly calculates what the stage value will be using value comparisons without if statements
        # gets the largest value that is still in range of the value of STAGE_MAX
        max_calc: int = min(STAGE_MAX, self.stage + stages)

        # gets the smallest value that is still in range of the value of STAGE_MIN
        min_calc: int = min(STAGE_MIN, self.stage - stages)

        # by comparing which of the two values is largest, the correctly adjusted value is returned
        self.stage: int = max(min_calc, max_calc)

    def apply_modifier(self) -> None:
        pass

    def to_dict(self) -> dict:
        data: dict = super().to_json()
        data['base_value'] = self.base_value
        data['value'] = self.value
        data['stage'] = self.stage
        data['modifier'] = self.modifier

        return data

    def from_dict(self, data: dict) -> Self:
        super().from_json(data)
        self.base_value = data['base_value']
        self.value = data['value']
        self.stage = data['stage']
        self.modifier = data['modifier']

        return self
