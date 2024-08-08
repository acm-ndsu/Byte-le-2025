from __future__ import annotations

from game.byte_2025.moves.effects import *
from game.common.enums import *


class Move(AbstractMove):
    def __init__(self, name: str = '', target_type: TargetType = TargetType.SINGLE_OPP, cost: int = 0,
                 effect: Effect | None = None):
        super().__init__(target_type)
        self.name: str = name
        self.object_type = ObjectType.MOVE
        self.cost: int = cost
        self.effect: Effect | None = effect

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
    def cost(self) -> int:
        return self.__cost

    @cost.setter
    def cost(self, cost: int) -> None:
        if cost is None or not isinstance(cost, int):
            raise ValueError(f'{self.__class__.__name__}.cost must be an int. It is a(n) {cost.__class__.__name__} '
                             f'and has the value of {cost}.')
        self.__cost: int = cost

    @property
    def effect(self) -> Effect | None:
        return self.__effect

    @effect.setter
    def effect(self, effect: Effect | None) -> None:
        if effect is not None and not isinstance(effect, Effect):
            raise ValueError(f'{self.__class__.__name__}.effect must be a Move or None. It is a(n) '
                             f'{effect.__class__.__name__} and has the value of {effect}.')
        self.__effect: Effect | None = effect

    def to_json(self) -> dict:
        data: dict = super().to_json()
        data['name'] = self.name
        data['cost'] = self.cost
        data['effect'] = self.effect.to_json() if self.effect is not None else None

        return data

    def from_json(self, data: dict) -> Self:
        super().from_json(data)
        self.name: str = data['name']
        self.cost: int = data['cost']

        if data['effect'] is None:
            self.effect: Effect | None = None
        else:
            if data['effect']['move_type'] == MoveType.MOVE:
                self.effect: Effect | None = Effect().from_json(data['effect'])
            elif data['effect']['move_type'] == MoveType.ATTACK:
                self.effect: AttackEffect | None = AttackEffect().from_json(data['effect'])
            elif data['effect']['move_type'] == MoveType.HEAL:
                self.effect: HealEffect | None = HealEffect().from_json(data['effect'])
            elif data['effect']['move_type'] == MoveType.BUFF:
                self.effect: BuffEffect | None = BuffEffect().from_json(data['effect'])
            elif data['effect']['move_type'] == MoveType.DEBUFF:
                self.effect: DebuffEffect | None = DebuffEffect().from_json(data['effect'])

        return self


class Attack(Move, AbstractAttack):
    def __init__(self, name: str = '', target_type: TargetType = TargetType.SINGLE_OPP, cost: int = 0,
                 effect: Move | None = None, damage_points: int = 0):
        super().__init__(name, target_type, cost, effect)

        self.damage_points: int = damage_points
        self.object_type = ObjectType.ATTACK
        self.move_type = MoveType.ATTACK


class Heal(Move, AbstractHeal):
    def __init__(self, name: str = '', target_type: TargetType = TargetType.ALL_ALLIES, cost: int = 0,
                 effect: Move | None = None, heal_points: int = 0):
        super().__init__(name, target_type, cost, effect)

        self.heal_points: int = heal_points
        self.object_type = ObjectType.HEAL
        self.move_type = MoveType.HEAL


class Buff(Move, AbstractBuff):
    def __init__(self, name: str = '', target_type: TargetType = TargetType.ALL_ALLIES, cost: int = 0,
                 effect: Effect | None = None, stage_amount: int = 1):
        super().__init__(name, target_type, cost, effect)

        self.stage_amount: int = stage_amount
        self.object_type = ObjectType.BUFF
        self.move_type = MoveType.BUFF


class Debuff(Move, AbstractDebuff):
    def __init__(self, name: str = '', target_type: TargetType = TargetType.SINGLE_OPP, cost: int = 0,
                 effect: Effect | None = None, stage_amount: int = -1):
        super().__init__(name, target_type, cost, effect)

        self.stage_amount: int = stage_amount
        self.object_type = ObjectType.DEBUFF
        self.move_type = MoveType.DEBUFF
