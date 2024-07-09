from typing import Self

from game.byte_2025.moves.move import Move
from game.common.enums import ObjectType, CharacterType, RankType
from game.common.game_object import GameObject
from game.utils.vector import Vector


class Character(GameObject):
    # PASSIVE NEEDS TO BE ABILITY | NONE

    """
    This is the superclass of all Character instances. Characters will have stats (health, attack, defense, speed);
    pre-determined moves that will allow for attacking, healing, buffing, and debuffing; and other properties that will
    help with the game mechanics.
    """

    def __init__(self, name: str = '', character_type: CharacterType = CharacterType.ATTACKER, health: int = 1,
                 attack: int = 1, defense: int = 1, speed: int = 1, guardian: Self | None = None,
                 possible_moves: dict[str: Move] = dict(), position: Vector | None = None):
        super().__init__()
        self.name: str = name
        self.object_type: ObjectType = ObjectType.CHARACTER
        self.character_type: CharacterType = character_type
        self.health: int = health
        self.attack: int = attack
        self.defense: int = defense
        self.speed: int = speed
        self.rank: RankType = RankType.GENERIC
        self.guardian: Self | None = guardian
        self.possible_moves: dict[str: Move] = possible_moves
        self.special_points: int = 0
        self.position: Vector | None = position

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        if name is None or not isinstance(name, str):
            raise ValueError(f'{self.__class__.__name__}.name must be a string. It is a(n) {name.__class__.__name__} '
                             f'and has the value of {name}')
        self.__name: str = name

    @property
    def character_type(self) -> CharacterType:
        return self.__character_type

    @character_type.setter
    def character_type(self, character_type: CharacterType) -> None:
        if CharacterType is None or not isinstance(character_type, CharacterType):
            raise ValueError(f'{self.__class__.__name__}.character_type must be a CharacterType. '
                             f'It is a(n) {character_type.__class__.__name__} and has the value of {character_type}')
        self.__character_type: CharacterType = character_type

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

        self.__health: int = health

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

        self.__attack: int = attack

    @property
    def defense(self) -> int:
        return self.__defense

    @defense.setter
    def defense(self, defense: int) -> None:
        if defense is None or not isinstance(defense, int):
            raise ValueError(f'{self.__class__.__name__}.defense must be an int. It is a(n) '
                             f'{defense.__class__.__name__} and has the value of {defense}')
        if defense < 0:
            raise ValueError(f'{self.__class__.__name__}.defense must be a positive int.')

        self.__defense: int = defense

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

        self.__speed: int = speed

    @property
    def guardian(self) -> Self | None:
        return self.__guardian

    @guardian.setter
    def guardian(self, guardian: Self | None) -> None:
        if guardian is not None and not isinstance(guardian, Character):
            raise ValueError(f'{self.__class__.__name__}.guardian must be a Character or None. It is a(n) '
                             f'{guardian.__class__.__name__} and has the value of {guardian}')

        self.__guardian: Character = guardian

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

        self.__special_points: int = special_points

    @property
    def position(self) -> Vector | None:
        return self.__position

    @position.setter
    def position(self, position: Vector | None) -> None:
        if position is not None and not isinstance(position, Vector):
            raise ValueError(f'{self.__class__.__name__}.position must be a Vector or None. It is a(n) '
                             f'{position.__class__.__name__} and has the value of {position}')

        self.__position: Vector = position

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
        self.name: str = data['name']
        self.character_type: CharacterType = data['character_type']
        self.health: int = data['health']
        self.attack: int = data['attack']
        self.defense: int = data['defense']
        self.speed: int = data['speed']
        self.rank: RankType = data['rank']
        self.guardian: Character = data['guardian']
        self.special_points: int = data['special_points']
        self.position: Vector = data['position']

        return self


class GenericAttacker(Character):
    def __init__(self, name: str = '', character_type: CharacterType = CharacterType.ATTACKER, health: int = 1,
                 attack: int = 1, defense: int = 1,
                 speed: int = 1, passive: None = None, guardian: Self | None = None,
                 possible_moves: dict[str: Move] = {}, position: Vector | None = None):
        super().__init__(name, character_type, health, attack, defense, speed, guardian, possible_moves, position)

        self.object_type: ObjectType = ObjectType.GENERIC_ATTACKER
        self.character_type: CharacterType = CharacterType.ATTACKER
        self.rank: RankType = RankType.GENERIC

    def to_json(self) -> dict:
        return super().to_json()

    def from_json(self, data: dict) -> Self:
        super().from_json(data)
        return self


class GenericHealer(Character):
    def __init__(self, name: str = '', character_type: CharacterType = CharacterType.HEALER, health: int = 1,
                 attack: int = 1, defense: int = 1,
                 speed: int = 1, passive: None = None, guardian: Self | None = None,
                 possible_moves: dict[str: Move] = {}, position: Vector | None = None):
        super().__init__(name, character_type, health, attack, defense, speed, guardian, possible_moves, position)

        self.object_type: ObjectType = ObjectType.GENERIC_HEALER
        self.character_type: CharacterType = CharacterType.HEALER
        self.rank: RankType = RankType.GENERIC

    def to_json(self) -> dict:
        return super().to_json()

    def from_json(self, data: dict) -> Self:
        super().from_json(data)
        return self


class GenericTank(Character):
    def __init__(self, name: str = '', character_type: CharacterType = CharacterType.TANK, health: int = 1,
                 attack: int = 1, defense: int = 1,
                 speed: int = 1, passive: None = None, guardian: Self | None = None,
                 possible_moves: dict[str: Move] = {}, position: Vector | None = None):
        super().__init__(name, character_type, health, attack, defense, speed, guardian, possible_moves, position)

        self.object_type: ObjectType = ObjectType.GENERIC_TANK
        self.character_type: CharacterType = CharacterType.TANK
        self.rank: RankType = RankType.GENERIC

    def to_json(self) -> dict:
        return super().to_json()

    def from_json(self, data: dict) -> Self:
        super().from_json(data)
        return self


class Leader(Character):
    def __init__(self, name: str = '', character_type: CharacterType = CharacterType.ATTACKER, health: int = 1,
                 attack: int = 1, defense: int = 1, speed: int = 1, guardian: Self | None = None,
                 possible_moves: dict[str: Move] = {}, special_points: int = 0, position: Vector | None = None,
                 passive: None = None):
        super().__init__(name, character_type, health, attack, defense, speed, guardian, possible_moves, position)

        self.object_type: ObjectType = ObjectType.LEADER
        self.rank: RankType = RankType.LEADER
        self.passive: None = None

    # PASSIVE GETTERS AND SETTERS

    def to_json(self) -> dict:
        data: dict = super().to_json()
        data['passive'] = self.passive
        return data

    def from_json(self, data: dict) -> Self:
        super().from_json(data)
        self.passive = data['passive']
        return self
