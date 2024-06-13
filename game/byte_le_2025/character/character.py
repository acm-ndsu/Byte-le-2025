from typing import Self

from game.common.enums import ObjectType, CharacterType, RankType
from game.common.game_object import GameObject
from game.utils.vector import Vector


class Character(GameObject):
    # PASSIVE NEEDS TO BE ABILITY | NONE
    # POSSIBLE MOVES NEEDS TO BE DICT[STR: MOVE]
    def __init__(self, name: str = '', character_type: CharacterType = CharacterType.ATTACKER, health: int = 1,
                 attack: int = 1, defense: int = 1, speed: int = 1, passive: None = None, guardian: Self | None = None,
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
        if name is None or not isinstance(name, str):
            raise ValueError(f'{self.__class__.__name__}.name must be a string. It is a(n) {name.__class__.__name__} '
                             f'and has the value of {name}')
        self.__name = name

    @property
    def character_type(self) -> CharacterType:
        return self.__character_type

    @character_type.setter
    def character_type(self, character_type: CharacterType) -> None:
        if CharacterType is None or not isinstance(character_type, CharacterType):
            raise ValueError(f'{self.__class__.__name__}.character_type must be a CharacterType. '
                             f'It is a(n) {character_type.__class__.__name__} and has the value of {character_type}')
        self.__character_type = character_type

    @property
    def health(self) -> int:
        return self.__health

    @health.setter
    def health(self, health: int) -> None:
        if health is None or not isinstance(health, int):
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
        if attack is None or not isinstance(attack, int):
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
        if defense is None or not isinstance(defense, int):
            raise ValueError(f'{self.__class__.__name__}.defense must be an int. It is a(n) '
                             f'{defense.__class__.__name__} and has the value of {defense}')
        if defense < 0:
            raise ValueError(f'{self.__class__.__name__}.health must be a positive int.')

        self.__defense = defense

    @property
    def speed(self) -> int:
        return self.__speed

    @speed.setter
    def speed(self, speed: int) -> None:
        if speed is None or not isinstance(speed, int):
            raise ValueError(f'{self.__class__.__name__}.speed must be an int. '
                             f'It is a(n) {speed.__class__.__name__} and has the value of {speed}')
        if speed < 0:
            raise ValueError(f'{self.__class__.__name__}.speed must be a positive int.')

        self.__speed = speed

    # PASSIVE GETTERS AND SETTERS

    @property
    def guardian(self) -> Self:
        return self.__guardian

    @guardian.setter
    def guardian(self, guardian: Self | None) -> None:
        if guardian is not None and not isinstance(guardian, Character):
            raise ValueError(f'{self.__class__.__name__}.held_item must be an Item or None. It is a(n) '
                             f'{guardian.__class__.__name__} and has the value of {guardian}')

        self.__guardian = guardian

    @property
    def special_points(self) -> int:
        return self.__special_points

    @special_points.setter
    def special_points(self, special_points: int) -> None:
        if special_points is None or not isinstance(special_points, int):
            raise ValueError(f'{self.__class__.__name__}.special_points must be an int. It is a(n) '
                             f'{special_points.__class__.__name__} and has the value of {special_points}')

        if special_points < 0:
            raise ValueError(f'{self.__class__.__name__}.special_points must be a positive int.')

        self.__special_points = special_points

    @property
    def position(self) -> Vector:
        return self.__position

    @position.setter
    def position(self, position: Vector | None) -> None:
        if position is not None and not isinstance(position, Vector):
            raise ValueError(f'{self.__class__.__name__}.position must be a Vector. It is a(n) '
                             f'{position.__class__.__name__} and has the value of {position}')

        self.__position = position

    def to_json(self) -> dict:
        data: dict = super().to_json()
        data['name'] = self.name
        data['character_type'] = self.character_type
        data['health'] = self.health
        data['attack'] = self.attack
        data['defense'] = self.defense
        data['speed'] = self.speed
        data['rank'] = self.rank
        data['guardian'] = self.guardian.to_json() if self.guardian is not None else None

        # change type hint once Move class is made
        # temp: dict = {}
        # data['possible_moves'] =

        data['special_points'] = self.special_points
        data['position'] = self.position if self.position is not None else None

        return data

    def from_json(self, data: dict) -> Self:
        super().from_json(data)
        self.name = data['name']
        self.character_type = data['character_type']
        self.health = data['health']
        self.attack = data['attack']
        self.defense = data['defense']
        self.speed = data['speed']
        self.rank = data['rank']
        self.guardian = data['guardian']
        self.special_points = data['special_points']
        self.position = data['position']

        return self
