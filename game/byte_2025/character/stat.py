from typing import Self

from game.common.game_object import GameObject


class Stat(GameObject):
    def __init__(self, base_value: int):
        super().__init__()
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
            raise TypeError(f'{self.__class__.__name__}.base_value must be an int. It is a(n) '
                            f'{base_value.__class__.__name__} and has a value of {base_value}')

        self.__base_value = base_value

    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int) -> None:
        if value is None or not isinstance(value, int):
            raise TypeError(f'{self.__class__.__name__}.value must be an int. It is a(n) '
                            f'{value.__class__.__name__} and has a value of {value}')

        self.__value = value

    @property
    def stage(self) -> int:
        return self.__stage

    @stage.setter
    def stage(self, stage: int) -> None:
        if stage is None or not isinstance(stage, int):
            raise TypeError(f'{self.__class__.__name__}.stage must be an int. It is a(n) '
                            f'{stage.__class__.__name__} and has a value of {stage}')

        if stage < -4 or stage > 4:
            raise ValueError(f'{self.__class__.__name__}.stage must be between -4 and 4 inclusive. The value given '
                             f'was {stage}')

        self.__stage = stage

    @property
    def modifier(self) -> float:
        return self.__modifier

    @modifier.setter
    def modifier(self, modifier: float) -> None:
        if modifier is None or not isinstance(modifier, float):
            raise TypeError(f'{self.__class__.__name__}.modifier must be a float. It is a(n) '
                            f'{modifier.__class__.__name__} and has a value of {modifier}')

        if modifier < 0.0 or modifier > 2.0:
            raise ValueError(f'{self.__class__.__name__}.modifier must be between 0.0 exclusive and 2.0 inclusive. The '
                             f'value given was {modifier}')

        self.__modifier = modifier

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
