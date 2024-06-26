from game.common.enums import *
from game.common.game_object import GameObject
from typing import Self


class Move(GameObject):

    def __init__(self, name: str = '', target_type: TargetType = TargetType.SINGLE_OPP, cost: int = 0, 
                 subaction: Self | None = None):
        super().__init__()
        self.name: str = name
        self.move_type: MoveType = MoveType.MOVE
        self.target_type: TargetType = target_type
        self.cost: int = cost
        self.subaction: Self | None = subaction

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        if name is None or not isinstance(name, str):
            raise ValueError(f'{self.__class__.__name__}.name must be a string. It is a(n) {name.__class__.__name__} '
                             f'and has the value of {name}.')
        self.__name: str = name

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
            raise ValueError(f'{self.__class__.__name__}.target_type must be a TargetType. It is a(n) {target_type.__class__.__name__} '
                             f'and has the value of {target_type}.')
        self.__target_type: TargetType = target_type

    @property
    def cost(self) -> int:
        return self.__cost

    @cost.setter
    def cost(self, cost: int) -> None:
        if cost is None or not isinstance(cost, int):
            raise ValueError(f'{self.__class__.__name__}.cost must be an int. It is a(n) {cost.__class__.__name__} '
                             f'and has the value of {cost}.')
        self.__cost: int = cost

    @property
    def subaction(self) -> Self | None:
        return self.__subaction

    @subaction.setter
    def subaction(self, subaction: Self | None) -> None:
        if subaction is not None and not isinstance(subaction, Move):
            raise ValueError(f'{self.__class__.__name__}.subaction must be a Move or None. It is a(n) '
                             f'{subaction.__class__.__name__} and has the value of {subaction}.')
        self.__subaction: Self | None = subaction

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
        if data['subaction'] is None:
            self.subaction: Self | None = None
        else:
            if data['subaction']['move_type'] == MoveType.MOVE:
                self.subaction: Self | None = Move().from_json(data['subaction'])
            elif data['subaction']['move_type'] == MoveType.ATTACK:
                self.subaction: Self | None = Attack().from_json(data['subaction'])
            elif data['subaction']['move_type'] == MoveType.HEAL:
                self.subaction: Self | None = Heal().from_json(data['subaction'])
            elif data['subaction']['move_type'] == MoveType.BUFF:
                self.subaction: Self | None = Buff().from_json(data['subaction'])
            elif data['subaction']['move_type'] == MoveType.DEBUFF:
                self.subaction: Self | None = Debuff().from_json(data['subaction'])
        return self


class Attack(Move):
    def __init__(self, name: str = '', target_type: TargetType = TargetType.SINGLE_OPP, cost: int = 0,
                 subaction: Move | None = None, damage_points: int = 0):
        super().__init__(name, target_type, cost, subaction)

        self.damage_points: int = damage_points
        self.move_type: MoveType = MoveType.ATTACK

    @property
    def damage_points(self) -> int:
        return self.__damage_points

    @damage_points.setter
    def damage_points(self, damage_points: int) -> None:
        if damage_points is None or not isinstance(damage_points, int):
            raise ValueError(f'{self.__class__.__name__}.damage_points must be an int. It is a(n) '
                             f'{damage_points.__class__.__name__} and has the value of {damage_points}.')
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
                 subaction: Move | None = None, heal_points: int = 0):
        super().__init__(name, target_type, cost, subaction)

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
    def buff_amount(self) -> float:
        return self.__buff_amount

    @buff_amount.setter
    def buff_amount(self, buff_amount: float) -> None:
        if buff_amount is None or not isinstance(buff_amount, float):
            raise ValueError(f'{self.__class__.__name__}.buff_amount must be a float. It is a(n) '
                             f'{buff_amount.__class__.__name__} and has the value of {buff_amount}.')
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
    def debuff_amount(self) -> float:
        return self.__debuff_amount

    @debuff_amount.setter
    def debuff_amount(self, debuff_amount: float) -> None:
        if debuff_amount is None or not isinstance(debuff_amount, float):
            raise ValueError(f'{self.__class__.__name__}.debuff_amount must be a float. It is a(n) '
                             f'{debuff_amount.__class__.__name__} and has the value of {debuff_amount}.')
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
