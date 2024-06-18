from game.common.enums import *


class Move:
    name: str
    move_type: MoveType
    target_type: TargetType
    cost: int
    #subaction: Move | None
    def use_move(targets = None)  -> None:
        pass

class Attack(Move):
    damage_points: int
    move_type: MoveType = MoveType.ATTACK


class Heal(Move):
    heal_points: float
    move_type: MoveType = MoveType.HEAL


class Buff(Move):
    modifier: float
    move_type: MoveType = MoveType.BUFF


class Debuff(Move):
    modifier: float
    move_type: MoveType = MoveType.DEBUFF
