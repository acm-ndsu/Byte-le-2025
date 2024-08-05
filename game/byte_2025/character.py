from __future__ import annotations

from game.byte_2025.moves.moves import *
from game.common.enums import ObjectType, CharacterType, RankType
from game.common.game_object import GameObject
from game.utils.vector import Vector


class Character(GameObject):
    # PASSIVE NEEDS TO BE ABILITY | NONE

    """
    This is the superclass of all Character instances. Characters will have 3 stats (health, defense, speed);
    pre-determined moves that will allow for attacking, healing, buffing, and debuffing; and other properties that will
    help with the game mechanics.
    """

    def __init__(self, name: str = '', character_type: CharacterType = CharacterType.ATTACKER, health: int = 1,
                 defense: int = 1, speed: int = 1, guardian: Self | None = None,
                 position: Vector | None = None, country_type: CountryType = CountryType.URODA):
        super().__init__()
        self.name: str = name
        self.object_type: ObjectType = ObjectType.CHARACTER
        self.character_type: CharacterType = character_type
        self.current_health: int = health
        self.max_health: int = health
        self.defense: int = defense
        self.speed: int = speed
        self.rank: RankType = RankType.GENERIC
        self.guardian: Self | None = guardian
        self.moveset: dict[str: Move] = dict()
        self.special_points: int = 0
        self.position: Vector | None = position
        self.took_action: bool = False
        self.country_type: CountryType = country_type

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
    def current_health(self) -> int:
        return self.__current_health

    @current_health.setter
    def current_health(self, current_health: int) -> None:
        if current_health is None or not isinstance(current_health, int):
            raise ValueError(f'{self.__class__.__name__}.current_health must be an int. It is a(n) '
                             f'{current_health.__class__.__name__} and has the value of {current_health}')
        if current_health < 0:
            raise ValueError(f'{self.__class__.__name__}.current_health must be a positive int.')

        self.__current_health: int = current_health

    @property
    def max_health(self) -> int:
        return self.__max_health

    @max_health.setter
    def max_health(self, max_health: int) -> None:
        if max_health is None or not isinstance(max_health, int):
            raise ValueError(f'{self.__class__.__name__}.max_health must be an int. It is a(n) '
                             f'{max_health.__class__.__name__} and has the value of {max_health}')
        if max_health < 0:
            raise ValueError(f'{self.__class__.__name__}.max_health must be a positive int.')

        self.__max_health: int = max_health

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
    def moveset(self) -> dict[str, Move]:
        return self.__moveset

    @moveset.setter
    def moveset(self, moveset: dict[str, Move]) -> None:
        if moveset is None or not isinstance(moveset, dict):
            raise ValueError(f'{self.__class__.__name__}.moveset must be a dict. It is a(n) {moveset.__class__.__name__} '
                             f'and has the value of {moveset}')

        # check if any of the keys in the dict are not a string
        if any([not isinstance(key, str) for key in moveset.keys()]):
            raise ValueError(f'{self.__class__.__name__}.moveset must be a dict with strings as the keys.')

        # check if any of the values in the dict are not a Move object
        if any([not isinstance(value, Move) for value in moveset.values()]):
            raise ValueError(f'{self.__class__.__name__}.moveset must be a dict with Move objects as the values.')

        self.__moveset: dict[str, Move] = moveset

    @property
    def position(self) -> Vector | None:
        return self.__position

    @position.setter
    def position(self, position: Vector | None) -> None:
        if position is not None and not isinstance(position, Vector):
            raise ValueError(f'{self.__class__.__name__}.position must be a Vector or None. It is a(n) '
                             f'{position.__class__.__name__} and has the value of {position}')

        self.__position: Vector = position

    @property
    def took_action(self) -> bool:
        return self.__took_action

    @took_action.setter
    def took_action(self, took_action: bool) -> None:
        if took_action is None or not isinstance(took_action, bool):
            raise ValueError(f'{self.__class__.__name__}.took_action must be a bool. It is a(n) '
                             f'{took_action.__class__.__name__} and has the value of {took_action}')

        self.__took_action = took_action

    @property
    def country_type(self) -> CountryType:
        return self.__country_type

    @country_type.setter
    def country_type(self, country_type: CountryType) -> None:
        if country_type is None or not isinstance(country_type, CountryType):
            raise ValueError(f'{self.__class__.__name__}.country_type must be a CountryType. '
                             f'It is a(n) {country_type.__class__.__name__} and has the value of {country_type}')
        self.__country_type: CountryType = country_type

    def get_na(self):
        return self.moveset['NA']

    def get_s1(self):
        return self.moveset['S1']

    def get_s2(self):
        return self.moveset['S2']

    def get_s3(self):
        return self.moveset['S3']

    def get_opposing_country(self) -> CountryType:
        # returns the opposite country based on the given CountryType
        return CountryType.URODA if self.country_type is CountryType.URODA else CountryType.TURPIS

    def to_json(self) -> dict:
        data: dict = super().to_json()
        data['name'] = self.name
        data['character_type'] = self.character_type
        data['current_health'] = self.current_health
        data['max_health'] = self.max_health
        data['defense'] = self.defense
        data['speed'] = self.speed
        data['rank'] = self.rank
        data['guardian'] = self.guardian.to_json() if self.guardian is not None else None
        data['moveset'] = {move_name: move.to_json() for move_name, move in self.moveset.items()}
        data['special_points'] = self.special_points
        data['position'] = self.position if self.position is not None else None
        data['took_action'] = self.took_action
        data['country_type'] = self.__country_type

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
            # case _:
                # raise ValueError(
                #     f'The object type of the object is not handled properly. The object type passed in is {temp}.')

    def from_json(self, data: dict) -> Self:
        super().from_json(data)
        self.name: str = data['name']
        self.character_type: CharacterType = data['character_type']
        self.current_health: int = data['current_health']
        self.max_health: int = data['max_health']
        self.defense: int = data['defense']
        self.speed: int = data['speed']
        self.rank: RankType = data['rank']
        self.guardian: Character = data['guardian']
        self.special_points: int = data['special_points']
        self.position: Vector = data['position']
        self.took_action = data['took_action']
        self.country_type = data['country_type']

        self.moveset: dict[str, Move] = {move_name: self.__from_json_helper(move)
                                         for move_name, move in data['moveset'].items()}

        return self


class GenericAttacker(Character):
    def __init__(self, name: str = '', character_type: CharacterType = CharacterType.ATTACKER, health: int = 1,
                 defense: int = 1, speed: int = 1, passive: None = None, guardian: Self | None = None,
                 position: Vector | None = None, country_type: CountryType = CountryType.URODA):
        super().__init__(name, character_type, health, defense, speed, guardian, position)

        self.object_type: ObjectType = ObjectType.GENERIC_ATTACKER
        self.character_type: CharacterType = CharacterType.ATTACKER
        self.rank: RankType = RankType.GENERIC
        self.country_type: CountryType = country_type

    def to_json(self) -> dict:
        return super().to_json()

    def from_json(self, data: dict) -> Self:
        super().from_json(data)
        return self


class GenericHealer(Character):
    def __init__(self, name: str = '', character_type: CharacterType = CharacterType.HEALER, health: int = 1,
                 defense: int = 1,
                 speed: int = 1, passive: None = None, guardian: Self | None = None,
                 position: Vector | None = None, country_type: CountryType = CountryType.URODA):
        super().__init__(name, character_type, health, defense, speed, guardian, position)

        self.object_type: ObjectType = ObjectType.GENERIC_HEALER
        self.character_type: CharacterType = CharacterType.HEALER
        self.rank: RankType = RankType.GENERIC
        self.country_type: CountryType = country_type

    def to_json(self) -> dict:
        return super().to_json()

    def from_json(self, data: dict) -> Self:
        super().from_json(data)
        return self


class GenericTank(Character):
    def __init__(self, name: str = '', character_type: CharacterType = CharacterType.TANK, health: int = 1,
                 defense: int = 1,
                 speed: int = 1, passive: None = None, guardian: Self | None = None,
                 position: Vector | None = None, country_type: CountryType = CountryType.URODA):
        super().__init__(name, character_type, health, defense, speed, guardian, position)

        self.object_type: ObjectType = ObjectType.GENERIC_TANK
        self.character_type: CharacterType = CharacterType.TANK
        self.rank: RankType = RankType.GENERIC
        self.country_type: CountryType = country_type

    def to_json(self) -> dict:
        return super().to_json()

    def from_json(self, data: dict) -> Self:
        super().from_json(data)
        return self


class Leader(Character):
    def __init__(self, name: str = '', character_type: CharacterType = CharacterType.ATTACKER, health: int = 1,
                 defense: int = 1, speed: int = 1, guardian: Self | None = None,
                 position: Vector | None = None, passive: None = None, country_type: CountryType = CountryType.URODA):
        super().__init__(name, character_type, health, defense, speed, guardian, position)

        self.object_type: ObjectType = ObjectType.LEADER
        self.rank: RankType = RankType.LEADER
        self.passive: None = None
        self.country_type: CountryType = country_type

    # PASSIVE GETTERS AND SETTERS

    def to_json(self) -> dict:
        data: dict = super().to_json()
        data['passive'] = self.passive
        return data

    def from_json(self, data: dict) -> Self:
        super().from_json(data)
        self.passive = data['passive']
        return self
