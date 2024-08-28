from __future__ import annotations

from game.byte_2025.character.stats import *
from game.byte_2025.moves.moves import *
from game.byte_2025.moves.moveset import Moveset
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
                 attack: AttackStat = AttackStat(), defense: DefenseStat = DefenseStat(1),
                 speed: SpeedStat = SpeedStat(1), guardian: Self | None = None,
                 position: Vector | None = None, country_type: CountryType = CountryType.URODA,
                 moveset: Moveset = Moveset()):
        super().__init__()
        self.name: str = name
        self.object_type: ObjectType = ObjectType.CHARACTER
        self.character_type: CharacterType = character_type
        self.current_health: int = health
        self.max_health: int = health
        self.attack: AttackStat = attack
        self.defense: DefenseStat = defense
        self.speed: SpeedStat = speed
        self.rank: RankType = RankType.GENERIC
        self.guardian: Self | None = guardian
        self.moveset: Moveset = moveset
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
    def attack(self) -> AttackStat:
        return self.__attack

    @attack.setter
    def attack(self, attack: AttackStat) -> None:
        if attack is None or not isinstance(attack, AttackStat):
            raise ValueError(f'{self.__class__.__name__}.attack must be an AttackStat. It is a(n) '
                             f'{attack.__class__.__name__} and has the value of {attack}')

        self.__attack: AttackStat = attack

    @property
    def defense(self) -> DefenseStat:
        return self.__defense

    @defense.setter
    def defense(self, defense: DefenseStat) -> None:
        if defense is None or not isinstance(defense, DefenseStat):
            raise ValueError(f'{self.__class__.__name__}.defense must be a DefenseStat. It is a(n) '
                             f'{defense.__class__.__name__} and has the value of {defense}')

        self.__defense: DefenseStat = defense

    @property
    def speed(self) -> SpeedStat:
        return self.__speed

    @speed.setter
    def speed(self, speed: SpeedStat) -> None:
        if speed is None or not isinstance(speed, SpeedStat):
            raise ValueError(f'{self.__class__.__name__}.speed must be a SpeedStat. '
                             f'It is a(n) {speed.__class__.__name__} and has the value of {speed}')

        self.__speed: SpeedStat = speed

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
    def moveset(self) -> Moveset:
        return self.__moveset

    @moveset.setter
    def moveset(self, moveset: Moveset) -> None:
        if moveset is None or not isinstance(moveset, Moveset):
            raise ValueError(f'{self.__class__.__name__}.moveset must be a Moveset. It is a(n) '
                             f'{moveset.__class__.__name__} and has the value of {moveset}')

        self.__moveset: Moveset = moveset

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

    def get_nm(self):
        return self.moveset.get_nm()

    def get_s1(self):
        return self.moveset.get_s1()

    def get_s2(self):
        return self.moveset.get_s2()

    def get_s3(self):
        return self.moveset.get_s3()

    def get_opposing_country(self) -> CountryType:
        # returns the opposite country based on the given CountryType
        return CountryType.URODA if self.country_type is CountryType.TURPIS else CountryType.TURPIS

    def to_json(self) -> dict:
        data: dict = super().to_json()
        data['name'] = self.name
        data['character_type'] = self.character_type
        data['current_health'] = self.current_health
        data['max_health'] = self.max_health
        data['attack'] = self.attack.to_json()
        data['defense'] = self.defense.to_json()
        data['speed'] = self.speed.to_json()
        data['rank'] = self.rank
        data['guardian'] = self.guardian.to_json() if self.guardian is not None else None
        data['moveset'] = self.moveset.to_json()
        data['special_points'] = self.special_points
        data['position'] = self.position.to_json() if self.position is not None else None
        data['took_action'] = self.took_action
        data['country_type'] = self.__country_type

        return data

    def __from_json_helper(self, data) -> Character:
        temp: ObjectType = ObjectType(data['object_type'])

        match ObjectType(data['object_type']):
            case ObjectType.GENERIC_ATTACKER:
                return GenericAttacker().from_json(data)
            case ObjectType.GENERIC_TANK:
                return GenericTank().from_json(data)
            case ObjectType.GENERIC_HEALER:
                return GenericHealer().from_json(data)
            case ObjectType.LEADER:
                return Leader().from_json(data)
            case _:
                raise ValueError(
                    f'The object type of the object is not handled properly. The object type passed in is {temp}.')

    def from_json(self, data: dict) -> Self:
        super().from_json(data)
        self.name: str = data['name']
        self.character_type: CharacterType = CharacterType(data['character_type'])
        self.current_health: int = data['current_health']
        self.max_health: int = data['max_health']
        self.attack: AttackStat = AttackStat().from_json(data['attack'])
        self.defense: DefenseStat = DefenseStat().from_json(data['defense'])
        self.speed: SpeedStat = SpeedStat().from_json(data['speed'])
        self.rank: RankType = RankType(data['rank'])
        self.guardian: Character = None if data['guardian'] is None else self.__from_json_helper(data['guardian'])
        self.moveset: Moveset = Moveset().from_json(data['moveset'])
        self.special_points: int = data['special_points']
        self.position: Vector | None = None if data['position'] is None else Vector().from_json(data['position'])
        self.took_action = data['took_action']
        self.country_type = CountryType(data['country_type'])

        return self


class GenericAttacker(Character):
    def __init__(self, name: str = '', character_type: CharacterType = CharacterType.ATTACKER, health: int = 1,
                 attack: AttackStat = AttackStat(), defense: DefenseStat = DefenseStat(1),
                 speed: SpeedStat = SpeedStat(1), guardian: Self | None = None,
                 position: Vector | None = None, country_type: CountryType = CountryType.URODA,
                 moveset: Moveset = Moveset()):
        super().__init__(name, character_type, health, attack, defense, speed,
                         guardian, position, country_type, moveset)

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
                 attack: AttackStat = AttackStat(), defense: DefenseStat = DefenseStat(1),
                 speed: SpeedStat = SpeedStat(1), guardian: Self | None = None,
                 position: Vector | None = None, country_type: CountryType = CountryType.URODA,
                 moveset: Moveset = Moveset()):
        super().__init__(name, character_type, health, attack, defense, speed,
                         guardian, position, country_type, moveset)

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
                 attack: AttackStat = AttackStat(), defense: DefenseStat = DefenseStat(1),
                 speed: SpeedStat = SpeedStat(1), guardian: Self | None = None,
                 position: Vector | None = None, country_type: CountryType = CountryType.URODA,
                 moveset: Moveset = Moveset()):
        super().__init__(name, character_type, health, attack, defense, speed,
                         guardian, position, country_type, moveset)

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
                 attack: AttackStat = AttackStat(), defense: DefenseStat = DefenseStat(1),
                 speed: SpeedStat = SpeedStat(1), guardian: Self | None = None,
                 position: Vector | None = None, passive: None = None, country_type: CountryType = CountryType.URODA,
                 moveset: Moveset = Moveset()):
        super().__init__(name, character_type, health, attack, defense, speed,
                         guardian, position, country_type, moveset)

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
