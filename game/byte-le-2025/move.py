from game.common.enums import *


class Move:
    name: str
    move_type: MoveType
    target_type: TargetType
    cost: int
    # use_move(targets = None): -> None
    # def use_move(targets = None)  -> None:


class Attack(Move):
    damage_points: int
    move_type: MoveType = MoveType.ATTACK
    subaction: Move | None


class Heal(Move):
    heal_points: float
    move_type: MoveType = MoveType.HEAL
    subaction: Move | None


class Buff(Move):
    modifier: float
    move_type: MoveType = MoveType.BUFF
    subaction: Move | None


class Debuff(Move):
    modifier: float
    move_type: MoveType = MoveType.DEBUFF
    subaction: Move | None
