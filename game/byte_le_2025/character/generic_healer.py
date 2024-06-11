from typing import Self

from character import Character
from game.common.enums import CharacterType, ObjectType, RankType
from game.utils.vector import Vector


class GenericHealer(Character):
    def __init__(self, name: str, character_type: CharacterType, health: int = 1, attack: int = 1, defense: int = 1,
                 speed: int = 1, passive: None = None, guardian: Self | None = None,
                 possible_moves: dict[str: None] = {}, special_points: int = 0, position: Vector | None = None):
        super().__init__(name, character_type, health, attack, defense, speed, passive, guardian, possible_moves,
                         special_points, position)

        self.object_type = ObjectType.GENERIC_HEALER
        self.character_type = CharacterType.HEALER
        self.rank = RankType.GENERIC

    def to_json(self) -> dict:
        return super().to_json()

    def from_json(self, data: dict) -> Self:
        super().from_json(data)
        return self
