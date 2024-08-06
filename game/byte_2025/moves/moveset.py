from __future__ import annotations

from game.byte_2025.moves.moves import *
from game.common.game_object import GameObject


class Moveset(GameObject):
    """
    A container class to represent every character's moveset. Helps with storing a character's moves in the JSON
    by removing that heavier logic from the Character class. Also prevents "mutable default value" warnings
    from other classes, making the code more robust.
    """

    def __init__(self, moves: tuple[Move, Move, Move, Move] = (Attack(), Buff(), Debuff(), Heal())):
        super().__init__()
        self.moves: dict[str, Move] = self.__tuple_to_dict(moves)

    @property
    def moves(self) -> dict[str, Move]:
        return self.__moves

    @moves.setter
    def moves(self, moves: dict[str, Move]) -> None:
        if moves is None or not isinstance(moves, dict):
            raise ValueError(
                f'{self.__class__.__name__}.moveset must be a dict. It is a(n) {moves.__class__.__name__} '
                f'and has the value of {moves}')

        # check if any of the keys in the dict are not a string
        if any([not isinstance(key, str) for key in moves.keys()]):
            raise ValueError(f'{self.__class__.__name__}.moveset must be a dict with strings as the keys.')

        # check if any of the values in the dict are not a Move object
        if any([not isinstance(value, Move) for value in moves.values()]):
            raise ValueError(f'{self.__class__.__name__}.moveset must be a dict with Move objects as the values.')

        # set the new dictionary
        self.__moves = moves

    def get_na(self) -> Move:
        return self.moves['NA']

    def get_s1(self) -> Move:
        return self.moves['S1']

    def get_s2(self) -> Move:
        return self.moves['S2']

    def get_s3(self) -> Move:
        return self.moves['S3']

    def __tuple_to_dict(self, moves: tuple[Move, Move, Move, Move]) -> dict[str, Move]:
        """
        Helper method to make the dict for the moveset.
        """
        keys: tuple[str, str, str, str] = ('NA', 'S1', 'S2', 'S3')
        return dict(zip(keys, moves))

    def to_json(self) -> dict:
        data: dict = super().to_json()
        data['moves'] = {move_name: move.to_json() for move_name, move in self.moves.items()}
        return data

    def __from_json_helper(self, data) -> Move:
        # temp: ObjectType = ObjectType(data['object_type'])

        match ObjectType(data['object_type']):
            case ObjectType.ATTACK:
                return Attack().from_json(data)
            case ObjectType.HEAL:
                return Heal().from_json(data)
            case ObjectType.BUFF:
                return Buff().from_json(data)
            case ObjectType.DEBUFF:
                return Debuff().from_json(data)
            case _:
                raise ValueError(f'{self.__class__.__name__}.__from_json_helper was not able to convert the given '
                                 f'ObjectType into a Move object: {data['object_type']}')

    def from_json(self, data: dict) -> Self:
        super().from_json(data)
        self.moves: dict[str, Move] = {move: self.__from_json_helper(data) for move, data in data['moves'].items()}

        return self
