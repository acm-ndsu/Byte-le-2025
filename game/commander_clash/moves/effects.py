from __future__ import annotations

from game.commander_clash.moves.abstract_moves import *
from game.common.enums import TargetType


class Effect(AbstractMove):
    """
    The Effect class - and any of its subclasses - behave as a secondary effect that occurs when a move is used. This
    can include inflicting damage to the user, giving a buff, providing additional healing, inflicting a debuff, and
    more. These inherit from AbstractMove since they have common attributes.
    """

    def __init__(self, target_type: TargetType = TargetType.SELF):
        super().__init__(target_type)
        self.object_type = ObjectType.EFFECT

    def to_json(self) -> dict:
        return super().to_json()

    def from_json(self, data: dict) -> Self:
        super().from_json(data)
        return self


class AttackEffect(AbstractAttack, Effect):
    def __init__(self, target_type: TargetType = TargetType.SELF, damage_points: int = 1):
        super().__init__(target_type, damage_points)
        self.object_type = ObjectType.ATTACK_EFFECT

    def to_json(self) -> dict:
        return super().to_json()

    def from_json(self, data: dict) -> Self:
        super().from_json(data)
        return self


class HealEffect(AbstractHeal, Effect):
    def __init__(self, target_type: TargetType = TargetType.SELF, heal_points: int = 0):
        super().__init__(target_type, heal_points)
        self.object_type = ObjectType.HEAL_EFFECT

    def to_json(self) -> dict:
        return super().to_json()

    def from_json(self, data: dict) -> Self:
        super().from_json(data)
        return self


class BuffEffect(AbstractBuff, Effect):
    def __init__(self, target_type: TargetType = TargetType.SELF, buff_amount: int = 1,
                 stat_to_affect: ObjectType = ObjectType.ATTACK_STAT):
        super().__init__(target_type, buff_amount, stat_to_affect)
        self.object_type = ObjectType.BUFF_EFFECT

    def to_json(self) -> dict:
        return super().to_json()

    def from_json(self, data: dict) -> Self:
        super().from_json(data)
        return self


class DebuffEffect(AbstractDebuff, Effect):
    def __init__(self, target_type: TargetType = TargetType.SELF, debuff_amount: int = -1,
                 stat_to_affect: ObjectType = ObjectType.ATTACK_STAT):
        super().__init__(target_type, debuff_amount, stat_to_affect)
        self.object_type = ObjectType.DEBUFF_EFFECT

    def to_json(self) -> dict:
        return super().to_json()

    def from_json(self, data: dict) -> Self:
        super().from_json(data)
        return self
