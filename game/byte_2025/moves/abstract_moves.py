from __future__ import annotations

from abc import abstractmethod
from typing import Self
from game.common.enums import *
from game.common.game_object import GameObject


class AbstractMove(GameObject):
    def __init__(self, target_type: TargetType = TargetType.SELF):
        super().__init__()
        self.object_type = ObjectType.ABSTRACT_MOVE
        self.move_type = MoveType.MOVE
        self.target_type = target_type

    @property
    def move_type(self) -> MoveType:
        return self.__move_type

    @move_type.setter
    def move_type(self, move_type: MoveType) -> None:
        if move_type is None or not isinstance(move_type, MoveType):
            raise ValueError(f'{self.__class__.__name__}.move_type must be a MoveType. It is a(n) '
                             f'{move_type.__class__.__name__} and has the value of {move_type}.')
        self.__move_type: MoveType = move_type

    @property
    def target_type(self) -> TargetType:
        return self.__target_type

    @target_type.setter
    def target_type(self, target_type: TargetType) -> None:
        if target_type is None or not isinstance(target_type, TargetType):
            raise ValueError(f'{self.__class__.__name__}.target_type must be a TargetType. It is a(n) '
                             f'{target_type.__class__.__name__} and has the value of {target_type}.')
        self.__target_type: TargetType = target_type

    @abstractmethod
    def use(self):
        pass

    def to_json(self) -> dict:
        data: dict = super().to_json()
        data['move_type'] = self.move_type
        data['target_type'] = self.target_type
        return data

    def from_json(self, data: dict) -> Self:
        super().from_json(data)
        self.move_type: MoveType = data['move_type']
        self.target_type: TargetType = data['target_type']
        return self


class AbstractAttack(AbstractMove):
    def __init__(self, target_type: TargetType = TargetType.SELF, damage_points: int = 0):
        super().__init__(target_type)
        self.damage_points: int = damage_points
        self.move_type = MoveType.ATTACK

    @property
    def damage_points(self) -> int:
        return self.__damage_points

    @damage_points.setter
    def damage_points(self, damage_points: int) -> None:
        if damage_points is None or not isinstance(damage_points, int):
            raise ValueError(f'{self.__class__.__name__}.damage_points must be an int. It is a(n) '
                             f'{damage_points.__class__.__name__} and has the value of {damage_points}.')
        self.__damage_points: int = damage_points

    @abstractmethod
    def use(self):
        pass

    def to_json(self) -> dict:
        data: dict = super().to_json()
        data['damage_points'] = self.damage_points
        return data

    def from_json(self, data: dict) -> Self:
        super().from_json(data)
        self.damage_points: int = data['damage_points']
        return self


class AbstractHeal(AbstractMove):
    def __init__(self, target_type: TargetType = TargetType.SELF, heal_points: int = 0):
        super().__init__(target_type)
        self.heal_points: int = heal_points
        self.move_type: MoveType = MoveType.HEAL

    @property
    def heal_points(self) -> int:
        return self.__heal_points

    @heal_points.setter
    def heal_points(self, heal_points: int) -> None:
        if heal_points is None or not isinstance(heal_points, int):
            raise ValueError(f'{self.__class__.__name__}.heal_points must be an int. It is a(n) '
                             f'{heal_points.__class__.__name__} and has the value of {heal_points}.')
        self.__heal_points: int = heal_points

    @abstractmethod
    def use(self):
        pass

    def to_json(self) -> dict:
        data: dict = super().to_json()
        data['heal_points'] = self.heal_points
        return data

    def from_json(self, data: dict) -> Self:
        super().from_json(data)
        self.heal_points: int = data['heal_points']
        return self


class AbstractBuff(AbstractMove):
    def __init__(self, target_type: TargetType = TargetType.SELF, buff_amount: float = 1.25):
        super().__init__(target_type)
        self.buff_amount: float = buff_amount
        self.move_type: MoveType = MoveType.BUFF

    @property
    def buff_amount(self) -> float:
        return self.__buff_amount

    @buff_amount.setter
    def buff_amount(self, buff_amount: float) -> None:
        if buff_amount is None or not isinstance(buff_amount, float):
            raise ValueError(f'{self.__class__.__name__}.buff_amount must be a float. It is a(n) '
                             f'{buff_amount.__class__.__name__} and has the value of {buff_amount}.')
        self.__buff_amount: float = buff_amount

    @abstractmethod
    def use(self) -> None:
        pass

    def to_json(self) -> dict:
        data: dict = super().to_json()
        data['buff_amount'] = self.buff_amount
        return data

    def from_json(self, data: dict) -> Self:
        super().from_json(data)
        self.buff_amount: int = data['buff_amount']
        return self


class AbstractDebuff(AbstractMove):
    def __init__(self, target_type: TargetType = TargetType.SELF, debuff_amount: float = 0.75):
        super().__init__(target_type)
        self.debuff_amount: float = debuff_amount
        self.move_type: MoveType = MoveType.DEBUFF

    @property
    def debuff_amount(self) -> float:
        return self.__debuff_amount

    @debuff_amount.setter
    def debuff_amount(self, debuff_amount: float) -> None:
        if debuff_amount is None or not isinstance(debuff_amount, float):
            raise ValueError(f'{self.__class__.__name__}.debuff_amount must be a float. It is a(n) '
                             f'{debuff_amount.__class__.__name__} and has the value of {debuff_amount}.')
        self.__debuff_amount: float = debuff_amount

    @abstractmethod
    def use(self) -> None:
        pass

    def to_json(self) -> dict:
        data: dict = super().to_json()
        data['debuff_amount'] = self.debuff_amount
        return data

    def from_json(self, data: dict) -> Self:
        super().from_json(data)
        self.debuff_amount: int = data['debuff_amount']
        return self
