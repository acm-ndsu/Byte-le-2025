from game.byte_2025.moves.abstract_moves import *
from game.common.enums import TargetType

"""
    Any of these submove classes behave as a secondary effect that occurs when a move is used. This can include 
    inflicting damage to the user, giving a buff, providing additional healing, inflicting a debuff, and more. 
    These classes are simpler version of the Move classes.
"""


class Submove(AbstractMove):
    def __init__(self, target_type: TargetType = TargetType.SELF):
        super().__init__(target_type)
        self.object_type = ObjectType.SUBMOVE

    def use(self):
        pass


class AttackSubmove(Submove, AbstractAttack):
    def __init__(self, target_type: TargetType = TargetType.SELF, damage_points: int = 0):
        super().__init__(target_type, damage_points)
        self.object_type = ObjectType.ATTACK_SUBMOVE

    def use(self):
        # MUST BE IMPLEMENTED
        pass


class HealSubmove(Submove, AbstractHeal):
    def __init__(self, target_type: TargetType = TargetType.SELF, heal_points: int = 0):
        super().__init__(target_type, heal_points)
        self.object_type = ObjectType.HEAL_SUBMOVE

    def use(self):
        # MUST BE IMPLEMENTED
        pass


class BuffSubmove(Submove, AbstractBuff):
    def __init__(self, target_type: TargetType = TargetType.SELF, buff_amount: float = 0.0):
        super().__init__(target_type, buff_amount)
        self.object_type = ObjectType.BUFF_SUBMOVE

    def use(self):
        # MUST BE IMPLEMENTED
        pass


class DebuffSubmove(Submove, AbstractDebuff):
    def __init__(self, target_type: TargetType = TargetType.SELF, debuff_amount: int = 0):
        super().__init__(target_type, debuff_amount)
        self.object_type = ObjectType.DEBUFF_SUBMOVE

    def use(self):
        # MUST BE IMPLEMENTED
        pass
