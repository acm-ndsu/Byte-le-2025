from game.common.enums import *
from game.common.game_object import GameObject
from typing import Self


class Move(GameObject):

    def __init__(self, name: str = '', target_type: TargetType = TargetType.SINGLE_OPP, cost: int = 0, 
                 subaction: Self | None = None):
        super().__init__()
        self.name: str = name
        self.move_type = MoveType.MOVE
        self.target_type: TargetType = target_type
        self.cost: int = cost
        self.subaction: Self | None = subaction

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        if name is None or not isinstance(name, str):
            raise ValueError(f'{self.__class__.__name__}.name must be a str. Name is currently'
                             f' a {name.__class__.__name__}.')
        self.__name: str = name

    @property
    def target_type(self) -> TargetType:
        return self.__target_type

    @target_type.setter
    def target_type(self, target_type: TargetType) -> None:
        if target_type is None or not isinstance(target_type, TargetType):
            raise ValueError(f'{self.__class__.__name__}.target_type bust be a Target_type. Target_type is currentlt '
                             f'a{target_type.__class__.__name__}.')
        self.__target_type: TargetType = target_type

    @property
    def cost(self) -> int:
        return self.__cost

    @cost.setter
    def cost(self, cost: int) -> None:
        if cost is None or not isinstance(cost, int):
            raise ValueError(f'{self.__class__.__name__}.cost must be a int. Cost is currently'
                             f' a {cost.__class__.__name__}.')
        self.__cost: int = cost

    @property
    def subaction(self):
        return self.__subaction

    @subaction.setter
    def subaction(self, subaction: Self | None) -> None:
        if subaction is not None and not isinstance(subaction, Move):
            raise ValueError(f'{self.__class__.__name__}.subaction must be a None. Subaction is currently'
                             f' a {subaction.__class__.__name__}.')
        self.__subaction: Self = subaction

    def use_move(self, targets=None) -> None:
        pass

    def to_json(self) -> dict:
        data: dict = super().to_json()
        data['name'] = self.name
        data['move_type'] = self.move_type
        data['target_type'] = self.target_type
        data['cost'] = self.cost
        data['subaction'] = self.subaction.to_json() if self.subaction is not None else None

        return data

    def from_json(self, data: dict) -> Self:
        super().from_json(data)
        self.name: str = data['name']
        self.move_type: MoveType = data['move_type']
        self.target_type: TargetType = data['target_type']
        self.cost: int = data['cost']
        self.subaction: Self | None = data['subaction']

        return self


class Attack(Move):
    def __init__(self, name: str = '', target_type: TargetType = TargetType.SINGLE_OPP, cost: int = 0,
                 subaction: Move | None = None, damage_points: int = 0):
        super().__init__(name, target_type, cost, subaction)

        self.damage_points: int = damage_points
        self.move_type: MoveType = MoveType.ATTACK

    @property
    def damage_points(self):
        return self.__damage_points

    @damage_points.setter
    def damage_points(self, damage_points: int):
        if damage_points is None or not isinstance(damage_points, int):
            raise ValueError(f'{self.__class__.__name__}.damage_points must be an int. Damage_points is currently'
                             f' a {damage_points.__class__.__name__}.')
        self.__damage_points: int = damage_points

    def use_move(self, targets=None) -> None:
        # IMPLEMENT HERE
        pass

    def to_json(self) -> dict:
        data: dict = super().to_json()
        data['damage_points'] = self.damage_points
        return data

    def from_json(self, data: dict) -> Self:
        super().from_json(data)
        self.damage_points: int = data['damage_points']
        return self


class Heal(Move):
    def __init__(self, name: str = '', target_type: TargetType = TargetType.SINGLE_ALLY, cost: int = 0,
                 subaction: Move | None = None, heal_points: float = 0.0):
        super().__init__(name, target_type, cost, subaction)

        self.heal_points: float = heal_points
        self.move_type: MoveType = MoveType.HEAL

    @property
    def heal_points(self):
        return self.__heal_points

    @heal_points.setter
    def heal_points(self, heal_points: float):
        if heal_points is None or not isinstance(heal_points, float):
            raise ValueError(f'{self.__class__.__name__}.heal_points must be an float. Heal_points is currently'
                             f' a {heal_points.__class__.__name__}.')
        self.__heal_points: float = heal_points

    def use_move(self, targets=None) -> None:
        pass

    def to_json(self) -> dict:
        data: dict = super().to_json()
        data['heal_points'] = self.heal_points
        return data

    def from_json(self, data: dict) -> Self:
        super().from_json(data)
        self.heal_points: int = data['heal_points']
        return self


class Buff(Move):
    def __init__(self, name: str = '', target_type: TargetType = TargetType.SINGLE_ALLY, cost: int = 0, 
                 subaction: Move | None = None, buff_amount: float = 0.0):
        super().__init__(name, target_type, cost, subaction)

        self.buff_amount: float = buff_amount
        self.move_type: MoveType = MoveType.BUFF

    @property
    def buff_amount(self):
        return self.__buff_amount

    @buff_amount.setter
    def buff_amount(self, buff_amount: float):
        if buff_amount is None or not isinstance(buff_amount, float):
            raise ValueError(f'{self.__class__.__name__}.buff_amount must be an float. Buff_amount is currently'
                             f' a {buff_amount.__class__.__name__}.')
        self.__buff_amount: float = buff_amount

    def use_move(self, targets=None) -> None:
        # IMPLEMENT HERE
        pass

    def to_json(self) -> dict:
        data: dict = super().to_json()
        data['buff_amount'] = self.buff_amount
        return data

    def from_json(self, data: dict) -> Self:
        super().from_json(data)
        self.buff_amount: int = data['buff_amount']
        return self


class Debuff(Move):
    def __init__(self, name: str = '', target_type: TargetType = TargetType.SINGLE_OPP, cost: int = 0,
                 subaction: Move | None = None, debuff_amount: float = 0.0):
        super().__init__(name, target_type, cost, subaction)

        self.debuff_amount: float = debuff_amount
        self.move_type: MoveType = MoveType.DEBUFF

    @property
    def debuff_amount(self):
        return self.__debuff_amount

    @debuff_amount.setter
    def debuff_amount(self, debuff_amount: float):
        if debuff_amount is None or not isinstance(debuff_amount, float):
            raise ValueError(f'{self.__class__.__name__}.debuff_amount must be an float. Debuff_amount is currently'
                             f' a {debuff_amount.__class__.__name__}.')
        self.__debuff_amount: float = debuff_amount

    def use_move(self, targets=None) -> None:
        # IMPLEMENT HERE
        pass

    def to_json(self) -> dict:
        data: dict = super().to_json()
        data['debuff_amount'] = self.debuff_amount
        return data

    def from_json(self, data: dict) -> Self:
        super().from_json(data)
        self.debuff_amount: int = data['debuff_amount']
        return self
