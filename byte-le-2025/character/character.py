from typing import Self

from game.common.enums import ObjectType, CharacterType, RankType
from game.common.game_object import GameObject
from game.utils.vector import Vector


class Character(GameObject):
    # PASSIVE NEEDS TO BE ABILITY | NONE
    # POSSIBLE MOVES NEEDS TO BE DICT[STR: MOVE]
    def __init__(self, name: str, character_type: CharacterType, health: int = 1, attack: int = 1, defense: int = 1,
                 speed: int = 1, passive: None = None, guardian: Self | None = None,
                 possible_moves: dict[str: None] = {}, special_points: int = 0, position: Vector | None = None):
        super().__init__()
        self.name = name
        self.object_type = ObjectType.CHARACTER
        self.character_type = character_type
        self.health = health
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.passive = passive
        self.rank = RankType.GENERIC
        self.guardian = guardian
        self.possible_moves = possible_moves
        self.special_points = special_points
        self.position = position

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        if not isinstance(name, str):
            raise ValueError(f'{self.__class__.__name__}.name must be a string. It is a(n) {name.__class__.__name__} '
                             f'and has the value of {name}')
        self.__name = name

    @property
    def character_type(self) -> CharacterType:
        return self.__character_type

    @character_type.setter
    def character_type(self, character_type: CharacterType) -> None:
        if not isinstance(character_type, CharacterType):
            raise ValueError(f'{self.__class__.__name__}.character_type must be a CharacterType. '
                             f'It is a(n) {character_type.__class__.__name__} and has the value of {character_type}')
        self.__character_type = character_type

    @property
    def health(self) -> int:
        return self.__health

    @health.setter
    def health(self, health: int) -> None:
        if not isinstance(health, int):
            raise ValueError(f'{self.__class__.__name__}.health must be an int. It is a(n) {health.__class__.__name__} '
                             f'and has the value of {health}')
        if health < 0:
            raise ValueError(f'{self.__class__.__name__}.health must be a positive int.')

        self.__health = health

    @property
    def attack(self) -> int:
        return self.__attack

    @attack.setter
    def attack(self, attack: int) -> None:
        if not isinstance(attack, int):
            raise ValueError(f'{self.__class__.__name__}.attack must be an int. '
                             f'It is a(n) {attack.__class__.__name__} and has the value of {attack}')
        if attack < 0:
            raise ValueError(f'{self.__class__.__name__}.attack must be a positive int.')

        self.__attack = attack

    @property
    def defense(self) -> int:
        return self.__defense

    @defense.setter
    def defense(self, defense: int) -> None:
        if not isinstance(defense, int):
            raise ValueError(f'{self.__class__.__name__}.defense must be an int. It is a(n) '
                             f'{defense.__class__.__name__} and has the value of {defense}')
        if defense < 0:
            raise ValueError(f'{self.__class__.__name__}.health must be a positive int.')

        self.__health = defense

    @property
    def speed(self) -> int:
        return self.__speed

    @speed.setter
    def speed(self, speed: int) -> None:
        if not isinstance(speed, int):
            raise ValueError(f'{self.__class__.__name__}.speed must be an int. '
                             f'It is a(n) {speed.__class__.__name__} and has the value of {speed}')
        if speed < 0:
            raise ValueError(f'{self.__class__.__name__}.speed must be a positive int.')

        self.__speed = speed

    # PASSIVE GETTERS AND SETTERS
