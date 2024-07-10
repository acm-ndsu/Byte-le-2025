from game.byte_2025.moves.submoves import *
from game.byte_2025.moves.abstract_moves import *
from game.common.enums import *


class Move(AbstractMove):
    def __init__(self, name: str = '', target_type: TargetType = TargetType.SINGLE_OPP, cost: int = 0,
                 submove: Submove | None = None):
        super().__init__(target_type)
        self.name: str = name
        self.object_type = ObjectType.MOVE
        self.cost: int = cost
        self.submove: Submove | None = submove

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
    def submove(self) -> Submove | None:
        return self.__submove

    @submove.setter
    def submove(self, submove: Submove | None) -> None:
        if submove is not None and not isinstance(submove, Submove):
            raise ValueError(f'{self.__class__.__name__}.submove must be a Move or None. It is a(n) '
                             f'{submove.__class__.__name__} and has the value of {submove}.')
        self.__submove: Submove | None = submove

    def use(self) -> None:
        pass

    def to_json(self) -> dict:
        data: dict = super().to_json()
        data['name'] = self.name
        data['cost'] = self.cost
        data['submove'] = self.submove.to_json() if self.submove is not None else None

        return data

    def from_json(self, data: dict) -> Self:
        super().from_json(data)
        self.name: str = data['name']
        self.cost: int = data['cost']

        if data['submove'] is None:
            self.submove: Submove | None = None
        else:
            if data['submove']['move_type'] == MoveType.MOVE:
                self.submove: Submove | None = Submove().from_json(data['submove'])
            elif data['submove']['move_type'] == MoveType.ATTACK:
                self.submove: Submove | None = AttackSubmove().from_json(data['submove'])
            elif data['submove']['move_type'] == MoveType.HEAL:
                self.submove: Submove | None = HealSubmove().from_json(data['submove'])
            elif data['submove']['move_type'] == MoveType.BUFF:
                self.submove: Submove | None = BuffSubmove().from_json(data['submove'])
            elif data['submove']['move_type'] == MoveType.DEBUFF:
                self.submove: Submove | None = DebuffSubmove().from_json(data['submove'])

        return self


class Attack(Move, AbstractAttack):
    def __init__(self, name: str = '', target_type: TargetType = TargetType.SINGLE_OPP, cost: int = 0,
                 submove: Move | None = None, damage_points: int = 0):
        super().__init__(name, target_type, cost, submove)

        self.damage_points: int = damage_points
        self.object_type = ObjectType.ATTACK


class Heal(Move, AbstractHeal):
    def __init__(self, name: str = '', target_type: TargetType = TargetType.SINGLE_ALLY, cost: int = 0,
                 submove: Move | None = None, heal_points: int = 0):
        super().__init__(name, target_type, cost, submove)

        self.heal_points: int = heal_points
        self.object_type = ObjectType.HEAL


class Buff(Move, AbstractBuff):
    def __init__(self, name: str = '', target_type: TargetType = TargetType.SINGLE_ALLY, cost: int = 0,
                 submove: Move | None = None, buff_amount: float = 0.0):
        super().__init__(name, target_type, cost, submove)

        self.buff_amount: float = buff_amount
        self.object_type = ObjectType.BUFF


class Debuff(Move, AbstractDebuff):
    def __init__(self, name: str = '', target_type: TargetType = TargetType.SINGLE_OPP, cost: int = 0,
                 submove: Move | None = None, debuff_amount: float = 0.0):
        super().__init__(name, target_type, cost, submove)

        self.debuff_amount: float = debuff_amount
        self.object_type = ObjectType.DEBUFF
