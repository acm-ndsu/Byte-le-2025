from game.byte_2025.moves.move import Move
from game.common.enums import ObjectType, TargetType, MoveType
from game.common.game_object import GameObject


class Submove(Move):
    """
    A Submove is a secondary action that occurs when a move is used. This can include inflicting damage to the user,
    giving a buff, providing additional healing, inflicting a debuff, and more. This class will *not* be allowed to
    have a submove object itself, despite
    """
    def __init__(self, target_type: TargetType = TargetType.SELF, move_type: MoveType = MoveType.BUFF):
        super().__init__(target_type=target_type)

        self.object_type = ObjectType.SUBMOVE
        self.move_type = move_type

    def __setattr__(self, key, value):
        if key in self.__dict__:
            raise AttributeError(f'Attribute {key} in {self.__class__.__name__} class cannot be changed.')

    def activate(self):
        """
        Will be called when a proper Move (attack, buff, etc.) is used. This is called "Activate" since this is
        treated like a secondary effect
        """
        pass

    def to_json(self) -> dict:
        return super().to_json()
