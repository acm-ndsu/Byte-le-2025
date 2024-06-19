from game.common.enums import *
from game.common.game_object import GameObject
from typing import Self


class Move(GameObject):

    def __init__(self, name: str = "", move_type: MoveType = MoveType.ATTACK,
                 target_type: TargetType = TargetType.SINGLE_OPP, cost: int = 0,
                 subaction: Self | None = None):
        super().__init__()
        self.name: str
        self.move_type: MoveType
        self.target_type: TargetType
        self.cost: int
        self.subaction: Self | None

    # GETTERS AND SETTERS
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        if name is None or not isinstance(name, str):
            raise ValueError(f'{self.__class__.__name__}.name must be a str. Name is currently a {name.__class__.__name__}.')
        self.__name: str = name

    def use_move(self, targets=None) -> None:
        pass

    # TO AND FROM JSON


class Attack(Move):
    def __init__(self, name: str = "", move_type: MoveType = MoveType.ATTACK,
                 target_type: TargetType = TargetType.SINGLE_OPP, cost: int = 0,
                 subaction: Self | None = None, damage_points: int = 0):
        super().__init__(name, move_type,
                 target_type, cost,
                 subaction)
        self.damage_points: int = damage_points

    def use_move(self, targets=None) -> None:
        # IMPLEMENT HERE
        pass


class Heal(Move):
    heal_points: float
    move_type: MoveType = MoveType.HEAL

    def use_move(self, targets=None) -> None:
        # IMPLEMENT HERE
        pass


class Buff(Move):
    modifier: float
    move_type: MoveType = MoveType.BUFF

    def use_move(self, targets=None) -> None:
        # IMPLEMENT HERE
        pass


class Debuff(Move):
    modifier: float
    move_type: MoveType = MoveType.DEBUFF

    def use_move(self, targets=None) -> None:
        # IMPLEMENT HERE
        pass
